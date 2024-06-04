import cppvariable as cvar
import pyramismap as pymap
import pytranslator as pyt
from logger import logger


class CPPFile:
    """
    Class to represent a C++ file. Objects of this class will be used to
    write to the output .cpp file.
    """

    maps = {}

    def __init__(self, filename):
        """
        Constructs a CPPFile object
        """
        self.filename = filename

        self.events = []  # list of pyramisevent

        self.lines = (
            ['#include "linkingheader.h"'] if not self.filename.endswith(".h") else []
        )  # hack. C++ code for entire file.

    def generate_header_files(self, finalIRContext):
        pmapHeaderlist = finalIRContext.map_access_history

        self.consolidate_map_headers(pmapHeaderlist)  # populate self.maps {}

        mapheaderfile = CPPFile("contexts.h")  # could be self.filename.h if multiple
        prequeltxt = f"#include <iostream>\n#include <iterator>\n#include <map>\n\nusing namespace std;\n\nmap<int, int> keyToFdMap;\nmap<int, pair<struct sockaddr_in *, int>> keyToIpFdMap;\n"
        mapheaderfile.lines.append(prequeltxt)

        # logger.debug(CPPFile.maps)
        for map in CPPFile.maps.values():
            # create map text:
            logger.debug(map.mapname)
            if not map.attributes:
                continue
            else:
                attrlist = map.attributes
                attrtxt = [f"{attr.type.type} {attr.name};\n" for attr in attrlist]
                attrtxt = "".join(attrtxt)

                text = f"\ntypedef struct {map.valuetype.type}{{\n{attrtxt}}}{map.valuetype.type}_t;\n\nmap<{map.keytype.type}, {map.valuetype.type}> {map.mapname};\n"
            mapheaderfile.lines.append(text)

        pyt.PyTranslator.output_files[mapheaderfile.filename] = mapheaderfile

        linkheaderfile = CPPFile("linkingheader.h")
        # use header.txt for preamble.
        with open("./UtilityFiles/header.txt") as ht:  # ./ means cwd
            preamble = ht.read()
            linkheaderfile.lines.append(preamble)

        # add mutex locks to linkingheader.h
        for map in CPPFile.maps.values():
            if not map.attributes:
                continue
            locktxt = f"extern pthread_mutex_t {map.mapname}Lock;\n"
            linkheaderfile.lines.append(locktxt)

        # Append Event Signatures. Event header param types MUST be inferred by this point.
        events = self.events

        for event in events:
            header = event.header
            returntype = header.returntype.typestr
            name = header.fname

            param_strings = []
            for param in header.parameters:
                param_strings.append(f"{param.type.typestr} {param.name}")

            param_string = ", ".join(param_strings)

            htext = f"\n{returntype} {name}({param_string});\n"
            linkheaderfile.lines.append(htext)

        # add hfile to translator file list
        pyt.PyTranslator.output_files[linkheaderfile.filename] = linkheaderfile

    def consolidate_map_headers(self, pmapHeaderDict):
        # check with stack

        for mapname, mapmetadata in pmapHeaderDict.items():  # All maps will be unique
            logger.debug(f"generating {mapname}")
            mapstores = mapmetadata["STORE"]  # List of PMAH objects
            maplookups = mapmetadata["LOOKUP"]

            # attr stored and subsequently/previously looked up
            pMAH_common_attr = []
            pMAH_redundant_attr = []
            pMAH_all_attr = []

            for pMAH in mapstores:
                # if any(pMAH.mapattr == pMAH_lookup.mapattr for pMAH_lookup in maplookups):
                #     pMAH_common_attr.append(pMAH)
                # if not any(pMAH.mapattr == pMAH_lookup.mapattr for pMAH_lookup in maplookups):
                #     pMAH_redundant_attr.append(pMAH)

                # only care about attr
                if pMAH.mapattr.type.type == "<TNF>":
                    # set to string
                    tp = cvar.CPPVariableType(type="string", ispointer=False)
                    pMAH.mapattr.type = tp
                pMAH_all_attr.append(pMAH)

            thismap = pymap.PyramisMap(mapname)
            # No optimisation
            if not pMAH_common_attr:
                logger.debug("Common")
                # pMAH_de_dup_all_attr = self.de_duplicate(pMAH_all_attr)
                for pMAH in pMAH_all_attr:
                    if pMAH.mapkey.name == "NULL":
                        pMAH.mapkey.type = cvar.CPPVariableType(
                            "string", ispointer=False
                        )
                    thismap.addkeyattrpair(pMAH.parent, pMAH.mapkey, pMAH.mapattr)

                # for pMAH in pMAH_de_dup_all_attr:
                #     thismap.addkeyattrpair(pMAH.parent, pMAH.mapkey, pMAH.mapattr)
            else:  # Add optimisation
                pMAH_de_dup_common_attr = self.de_duplicate(pMAH_common_attr)
                for pMAH in pMAH_de_dup_common_attr:
                    thismap.addkeyattrpair(pMAH.parent, pMAH.mapkey, pMAH.mapattr)

            for pMAH in pMAH_redundant_attr:
                rline = pMAH.line_no
                rfunc = pMAH.parent
                # find functioncall at that lineno
                calls = self.function_definitions[
                    rfunc
                ]  # funcdef containing redundant store
                # del calls.functioncalls[rline]

            CPPFile.maps[mapname] = thismap

            assert type(CPPFile.maps[mapname] is pymap.PyramisMap)
