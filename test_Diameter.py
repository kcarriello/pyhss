import unittest
import requests
import json
import logging
import sys
global log
log= logging.getLogger("UnitTestLogger")
import diameter as DiameterLib
import traceback

class Diameter_Tests(unittest.TestCase):
    diameter_inst = 0
    Diameter_CER = b"\x01\x00\x01P\x80\x00\x01\x01\x00\x00\x00\x00\x8e\xb7\xd5j\xb0{\xcd\xd6\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00\x00\x00\x01\x01@\x00\x00\x0e\x00\x01\x7f\x00\x01\x01\x00\x00\x00\x00\x01\n@\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x01\r\x00\x00\x00\x14PyHSS-client\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00#\x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00\x16\x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00'\x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00\x01\x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00\x00\x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x02@\x00\x00\x0c\xff\xff\xff\xff\x00\x00\x01\t@\x00\x00\x0c\x00\x00\x15\x9f\x00\x00\x01\t@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\t@\x00\x00\x0c\x00\x002\xdb"
    Diameter_DWR = b'\x01\x00\x00P\x80\x00\x01\x18\x00\x00\x00\x00x\xb7\x96\x8du\xb2+\xf3\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00'
    Diameter_DPR = b'0100008c8000011a000000009aeff2238170f971000001084000003a696c7363303364737230312e6d766e6f2e6570632e6d6e633538382e6d63633331312e336770706e6574776f726b2e6f72670000000001284000002e6d766e6f2e6570632e6d6e633538382e6d63633331312e336770706e6574776f726b2e6f72670000000001114000000c00000000'
    Diameter_AIR = b"\x01\x00\x01\x14\xc0\x00\x01>\x01\x00\x00#0\xd0hym\x19i\xc8\x00\x00\x01\x07@\x00\x00'6873733031;3076d64228;1;app_s6a\x00\x00\x00\x01\x15@\x00\x00\x0c\x00\x00\x00\x01\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00\x00\x00\x01\x1b@\x00\x00\x1cnickvsnetworking.com\x00\x00\x00\x01@\x00\x00\x17505931111111116\x00\x00\x00\x05\x80\xc0\x00\x00,\x00\x00(\xaf\x00\x00\x05\x82\xc0\x00\x00\x10\x00\x00(\xaf\x00\x00\x00\x01\x00\x00\x05\x84\xc0\x00\x00\x10\x00\x00(\xaf\x00\x00\x00\x01\x00\x00\x05\x7f\xc0\x00\x00\x0f\x00\x00(\xaf\x05\xf59\x00\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00#"
    Diameter_ULR = b"\x01\x00\x01\x18\xc0\x00\x01<\x01\x00\x00#\xa2\xd9\xb6\\\xe9!\xf7\xfa\x00\x00\x01\x07@\x00\x00'6873733031;c78c1d986e;1;app_s6a\x00\x00\x00\x01\x15@\x00\x00\x0c\x00\x00\x00\x01\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00\x00\x00\x01\x1b@\x00\x00\x1cnickvsnetworking.com\x00\x00\x00\x01@\x00\x00\x17505931111111116\x00\x00\x00\x04\x08\x80\x00\x00\x10\x00\x00(\xaf\x00\x00\x03\xec\x00\x00\x05}\xc0\x00\x00\x10\x00\x00(\xaf\x00\x00\x00\x02\x00\x00\x05\x7f\xc0\x00\x00\x0f\x00\x00(\xaf\x05\xf59\x00\x00\x00\x06O\x80\x00\x00\x10\x00\x00(\xaf\x00\x00\x00\x00\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00#"
    Diameter_PUR = b"\x01\x00\x00\xc4\xc0\x00\x01A\x01\x00\x00#\xf2\xdc\x8e/\xf6*\xfa\xe1\x00\x00\x01\x07@\x00\x00'6873733031;485307f5f1;1;app_s6a\x00\x00\x00\x01\x15@\x00\x00\x0c\x00\x00\x00\x01\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00\x00\x00\x01\x1b@\x00\x00\x08\x00\x00\x00\x01@\x00\x00\x17505931111111116\x00\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00#"
    Diameter_CLR = b"\x01\x00\x00\xd4\xc0\x00\x01=\x01\x00\x00#\xcd\x17\xde\xfd@j7\xee\x00\x00\x01\x07@\x00\x00'6873733031;ed09a5fb06;1;app_s6a\x00\x00\x00\x01\x15@\x00\x00\x0c\x00\x00\x00\x01\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00\x00\x00\x01\x1b@\x00\x00\x08\x00\x00\x00\x01@\x00\x00\x17505931111111116\x00\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00#\x00\x00\x05\x8c\xc0\x00\x00\x10\x00\x00(\xaf\x00\x00\x00\x02"
    Diameter_DPR = b'\x01\x00\x00\\\x80\x00\x01\x1a\x00\x00\x00\x007%\x1fT\x13j\xdf\x14\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00\x00\x00\x01\x11@\x00\x00\x0c\x00\x00\x00\x00'


    Diameter_Cx_MAA = b'\x01\x00\x01h\xc0\x00\x01/\x01\x00\x00\x00\xc1Dg\xeb\xdd\xeebn\x00\x00\x01\x07@\x00\x00&6873733031;53ca4d5113;1;app_cx\x00\x00\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00\x00\x00\x01\x1b@\x00\x00\x13localdomain\x00\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00\x00\x00\x00\x01\x15@\x00\x00\x0c\x00\x00\x00\x01\x00\x00\x00\x01@\x00\x00,505931111111116@nickvsnetworking.com\x00\x00\x02Y\xc0\x00\x004\x00\x00(\xafsip:505931111111116@nickvsnetworking.com\x00\x00\x02_\xc0\x00\x00\x10\x00\x00(\xaf\x00\x00\x00\x01\x00\x00\x02d\xc0\x00\x00(\x00\x00(\xaf\x00\x00\x02`\xc0\x00\x00\x1c\x00\x00(\xafDigest-AKAv1-MD5\x00\x00\x02Z\xc0\x00\x00\x18\x00\x00(\xafPyHSS-client'
    Diameter_Cx_UAR = b'\x01\x00\x018\xc0\x00\x01,\x01\x00\x00\x00g|%\xa6\x92h!\xea\x00\x00\x01\x07@\x00\x00&6873733031;d01955b4ab;1;app_cx\x00\x00\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00\x00\x00\x01\x1b@\x00\x00\x13localdomain\x00\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00\x00\x00\x00\x01\x15@\x00\x00\x0c\x00\x00\x00\x01\x00\x00\x00\x01@\x00\x00,505931111111116@nickvsnetworking.com\x00\x00\x02Y\xc0\x00\x004\x00\x00(\xafsip:505931111111116@nickvsnetworking.com\x00\x00\x02X\xc0\x00\x00 \x00\x00(\xafnickvsnetworking.com'
    Diameter_Cx_SAR = b'\x01\x00\x01p\xc0\x00\x01-\x01\x00\x00\x00\x8b(\xf6\x1b\xd2\x1df\xc4\x00\x00\x01\x07@\x00\x00&6873733031;805d6d645b;1;app_cx\x00\x00\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00\x00\x00\x01\x1b@\x00\x00\x13localdomain\x00\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00\x00\x00\x00\x01\x15@\x00\x00\x0c\x00\x00\x00\x01\x00\x00\x02Y\xc0\x00\x004\x00\x00(\xafsip:505931111111116@nickvsnetworking.com\x00\x00\x02Z\xc0\x00\x007\x00\x00(\xafsip:scscf.mnc001.mcc01.3gppnetwork.org:5060\x00\x00\x00\x00\x01@\x00\x00,505931111111116@nickvsnetworking.com\x00\x00\x02f\xc0\x00\x00\x10\x00\x00(\xaf\x00\x00\x00\x01\x00\x00\x02p\xc0\x00\x00\x10\x00\x00(\xaf\x00\x00\x00\x00'
    Diameter_Cx_RTR = b'\x01\x00\x01\xc4\xc0\x00\x010\x01\x00\x00\x00\x8c\xbb\xca\xee-;j"\x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00#\x00\x00\x01\x07@\x00\x00&6873733031;89382efa9e;1;app_cx\x00\x00\x00\x00\x01\x04@\x00\x00 \x00\x00\x01\x02@\x00\x00\x0c\x01\x00\x00\x00\x00\x00\x01\n@\x00\x00\x0c\x00\x00(\xaf\x00\x00\x01\x08@\x00\x00\rhss01\x00\x00\x00\x00\x00\x01(@\x00\x00)epc.mnc001.mcc001.3gppnetwork.org\x00\x00\x00\x00\x00\x02g\xc0\x00\x004\x00\x00(\xaf\x00\x00\x02h\xc0\x00\x00\x10\x00\x00(\xaf\x00\x00\x00\x00\x00\x00\x02i\xc0\x00\x00\x17\x00\x00(\xafTest Reason\x00\x00\x00\x01\x1b@\x00\x00\x13localdomain\x00\x00\x00\x01%@\x00\x00\x17hss.localdomain\x00\x00\x00\x01\x15@\x00\x00\x0c\x00\x00\x00\x01\x00\x00\x00\x01@\x00\x00,505931111111116@nickvsnetworking.com\x00\x00\x02Y\xc0\x00\x004\x00\x00(\xafsip:505931111111116@nickvsnetworking.com\x00\x00\x02Z\xc0\x00\x00\x18\x00\x00(\xafPyHSS-client\x00\x00\x01\x1c@\x00\x00(\x00\x00\x01\x18@\x00\x00\x13localdomain\x00\x00\x00\x00!@\x00\x00\n\x00\x01\x00\x00\x00\x00\x01\x1a@\x00\x00\x13localdomain\x00'

    #Test IMSI - 505931111111116

    def test_A_Instantiate(self):
        diameter_inst = DiameterLib.Diameter(
            str('OriginHost'), str('OriginRealm'), 
            str('UnitTest_Diameter'), str('001'), str('001')
        )
        log.debug("Instantiated Diameter Class")
        self.__class__.diameter_inst = diameter_inst
        self.assertEqual(isinstance(diameter_inst, DiameterLib.Diameter), True, "Created Class OK")
        
    def test_B_Recv_CER_CmdCode(self):
        packet_vars, avps = self.__class__.diameter_inst.decode_diameter_packet(self.__class__.Diameter_CER)
        log.debug("Received request with Command Code: " + str(packet_vars['command_code']) + ", ApplicationID: " + str(packet_vars['ApplicationId']) + " and flags " + str(packet_vars['flags']))
        self.assertEqual(packet_vars['command_code'], 257, "Command Code Mismatch")

    def test_B_Recv_CER_ApplicationID(self):
        packet_vars, avps = self.__class__.diameter_inst.decode_diameter_packet(self.__class__.Diameter_CER)
        self.assertEqual(packet_vars['ApplicationId'], 0, "Application ID Mismatch")

    def test_B_Recv_AIR(self):
        packet_vars, avps = self.__class__.diameter_inst.decode_diameter_packet(self.__class__.Diameter_AIR)
        log.debug("Received request with Command Code: " + str(packet_vars['command_code']) + ", ApplicationID: " + str(packet_vars['ApplicationId']) + " and flags " + str(packet_vars['flags']))
        if packet_vars['command_code'] == 318 and packet_vars['ApplicationId'] == 16777251 and packet_vars['flags'] == "c0":
                log.info("Received Request with command code 318 (3GPP Authentication-Information-Request) - Generating (AIA)")
                try:
                    response = self.__class__.diameter_inst.Answer_16777251_318(packet_vars, avps)      #Generate Diameter packet
                    log.info("Generated AIR")
                except Exception as e:
                    log.info("Failed to generate Diameter Response for AIR")
                    log.info(e)
                    traceback.print_exc()
                    log.info("Generated DIAMETER_USER_DATA_NOT_AVAILABLE AIR")

        self.assertEqual(packet_vars['ApplicationId'], 0, "Application ID Mismatch")

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger("UnitTestLogger").setLevel( logging.DEBUG )
    unittest.main()