from TextCoordinate import ItemCoordinate, HeaderList, PdfProperties


class PdfCollection:
    def __init__(self):
        self.collection: PdfProperties = []
        self.add()
        pass

    def add(self):
        self.collection = [
            PdfProperties(
                1,
                "Sample documents/New folder/123 Ink.pdf",
                1,
                [
                    HeaderList(1, "QUANTITY", [ItemCoordinate(144, 1076, 380, 1111)]),
                    HeaderList(2, "SKU", [ItemCoordinate(373, 1063, 673, 1108)]),
                    HeaderList(3, "DESCRIPTION", [ItemCoordinate(673, 1063, 1646, 1111)]),
                    HeaderList(4, "VAT", [ItemCoordinate(1659, 1063, 1843, 1105)]),
                    HeaderList(5, "UNIT PRICE", [ItemCoordinate(1846, 1066, 2091, 1111)]),
                    HeaderList(6, "TOTAL", [ItemCoordinate(2091, 1063, 2339, 1101)])
                ]
            ),
            PdfProperties(
                2,
                "Sample documents/New folder/ACP Limited.pdf",
                1,
                [
                    HeaderList(1, "Quality", [ItemCoordinate(128, 1249, 357, 1339)]),
                    HeaderList(2, "Description", [ItemCoordinate(360, 1243, 1278, 1336)]),
                    HeaderList(3, "Unit Price", [ItemCoordinate(1301, 1246, 1684, 1333)]),
                    HeaderList(4, "Net Amt", [ItemCoordinate(1694, 1243, 1935, 1336)]),
                    HeaderList(5, "VAT %", [ItemCoordinate(1945, 1246, 2167, 1336)]),
                    HeaderList(6, "VAT", [ItemCoordinate(2177, 1249, 2360, 1339)])
                ]
            ),
            PdfProperties(
                3,
                "Sample documents/New folder/M. KELLIHER 1998 Ltd. 3 Page.pdf",
                1,
                [
                    HeaderList(1, "Item Number", [ItemCoordinate(109, 1554, 467, 1620)]),
                    HeaderList(2, "Config No.", [ItemCoordinate(477, 1557, 712, 1617)]),
                    HeaderList(3, "Description", [ItemCoordinate(712, 1561, 1289, 1620)]),
                    HeaderList(4, "Qty", [ItemCoordinate(1295, 1567, 1395, 1617)]),
                    HeaderList(5, "Net selling price", [ItemCoordinate(1398, 1464, 1597, 1617)]),
                    HeaderList(6, "Unit", [ItemCoordinate(1607, 1534, 1769, 1617)]),
                    HeaderList(6, "VAT", [ItemCoordinate(1783, 1551, 1938, 1614)]),
                    HeaderList(6, "WEEE", [ItemCoordinate(1952, 1554, 2131, 1617)]),
                    HeaderList(6, "Net Total", [ItemCoordinate(2134, 1557, 2326, 1614)]),
                ],
                8
            ),
            PdfProperties(
                4,
                "Sample documents/New folder/AccurA Diamond Tools Ltd.pdf",
                1,
                [
                    HeaderList(1, "Qty", [ItemCoordinate(135, 1265, 251, 1326)]),
                    HeaderList(2, "Code", [ItemCoordinate(280, 1259, 560, 1317)]),
                    HeaderList(3, "Product Description", [ItemCoordinate(570, 1259, 1307, 1314)]),
                    HeaderList(4, "Unit Price", [ItemCoordinate(1333, 1265, 1732, 1314)]),
                    HeaderList(5, "Net Amount", [ItemCoordinate(1742, 1268, 2064, 1314)]),
                    HeaderList(6, "VAT Amount", [ItemCoordinate(2087, 1259, 2373, 1317)])
                ]
            ),
            PdfProperties(
                5,
                "Sample documents/New folder/Thomas Archer (Ballina) 2 Page.pdf",
                1,
                [
                    HeaderList(1, "Item Code", [ItemCoordinate(74, 1198, 354, 1307)]),
                    HeaderList(2, "Description", [ItemCoordinate(376, 1201, 1101, 1310)]),
                    HeaderList(3, "Quantity", [ItemCoordinate(1095, 1198, 1326, 1304)]),
                    HeaderList(4, "UOM", [ItemCoordinate(1320, 1198, 1516, 1304)]),
                    HeaderList(5, "Unit Price", [ItemCoordinate(1516, 1198, 1710, 1304)]),
                    HeaderList(6, "Amount", [ItemCoordinate(1713, 1194, 1955, 1304)]),
                    HeaderList(7, "Dis %", [ItemCoordinate(1955, 1198, 2106, 1310)]),
                    HeaderList(8, "Line Total", [ItemCoordinate(2109, 1198, 2383, 1310)])
                ]
            ),
            PdfProperties(
                6,
                "Sample documents/New folder/Chadwicks 2 Page.pdf",
                1,
                [
                    HeaderList(1, "ITEM", [ItemCoordinate(67, 1285, 238, 1398)]),
                    HeaderList(2, "QTY", [ItemCoordinate(244, 1285, 412, 1401)]),
                    HeaderList(3, "UNIT", [ItemCoordinate(422, 1285, 586, 1395)]),
                    HeaderList(4, "DESCRIPTION", [ItemCoordinate(589, 1285, 1598, 1391)]),
                    HeaderList(5, "EXCL. VAT", [ItemCoordinate(1601, 1285, 1833, 1391)]),
                    HeaderList(6, "EXCL. VAT", [ItemCoordinate(1836, 1282, 2071, 1395)]),
                    HeaderList(7, "INCL.VAT", [ItemCoordinate(2075, 1282, 2300, 1398)]),
                    HeaderList(8, "CODE", [ItemCoordinate(2303, 1288, 2423, 1398)])
                ]
            ),
            PdfProperties(
                7,
                "Sample documents/New folder/PF 3 Page.pdf",
                1,
                [
                    HeaderList(1, "Item", [ItemCoordinate(115, 1059, 357, 1162)]),
                    HeaderList(2, "Name", [ItemCoordinate(357, 1059, 1732, 1156)]),
                    HeaderList(3, "Quantity", [ItemCoordinate(1732, 1062, 1974, 1156)]),
                    HeaderList(4, "Price", [ItemCoordinate(1977, 1059, 2174, 1162)]),
                    HeaderList(5, "Total", [ItemCoordinate(2177, 1066, 2367, 1156)])
                ]
            ),
            PdfProperties(
                8,
                "Sample documents/New folder/Harlow Agencies Limited.pdf",
                1,
                [
                    HeaderList(1, "Item Code", [ItemCoordinate(63.8, 1061, 505, 1134)]),
                    HeaderList(2, "Description", [ItemCoordinate(505, 1070, 1572, 1121)]),
                    HeaderList(3, "Quantity", [ItemCoordinate(1567, 1061, 1850.2, 1125.61)]),
                    HeaderList(4, "UOM", [ItemCoordinate(1854, 1061, 2150, 1134)]),
                    HeaderList(5, "Unit Price", [ItemCoordinate(2155, 1057, 2460, 1130)]),
                    HeaderList(6, "Amount", [ItemCoordinate(2469, 1061, 2807, 1134)]),
                    HeaderList(7, "Dis %", [ItemCoordinate(2816, 1061, 3030, 1134)]),
                    HeaderList(8, "Line Total", [ItemCoordinate(3044, 1070, 3349.5, 1130)])
                ]
            ),
            PdfProperties(
                9,
                "Sample documents/New folder/Aereco Ltd.pdf",
                1,
                [
                    HeaderList(1, "Serial", [ItemCoordinate(99.84, 1494.44, 177.14, 1558.85)]),
                    HeaderList(2, "Reference", [ItemCoordinate(180.36, 1491.22, 409.03, 1558.85)]),
                    HeaderList(3, "Description", [ItemCoordinate(447, 1491.22, 1661.92, 1555.63)]),
                    HeaderList(4, "Quantity", [ItemCoordinate(1671.58, 1494.44, 1929.24, 1555.63)]),
                    HeaderList(5, "Unit Price", [ItemCoordinate(1942.12, 1494.44, 2193.35, 1555.63)]),
                    HeaderList(6, "Total", [ItemCoordinate(2203, 1494.44, 2354.38, 1555.63)])
                ]
            ),
            PdfProperties(
                10,
                "Sample documents/New folder/Alupress Ltd.pdf",
                5,
                [
                    HeaderList(1, "Description", [ItemCoordinate(106.32, 1201.83, 1259.83, 1275.94)]),
                    HeaderList(2, "Quantity", [ItemCoordinate(1272.72, 1208.27, 1543.37, 1275.94)]),
                    HeaderList(3, "Unit Price", [ItemCoordinate(1569.15, 1205.05, 1865.58, 1275.94)]),
                    HeaderList(4, "Tax", [ItemCoordinate(1907.47, 1198.61, 2062.12, 1275.94)]),
                    HeaderList(5, "Amount EUR", [ItemCoordinate(2087.90, 1195.39, 2381.11, 1275.94)])
                ]
            ),
            PdfProperties(
                11,
                "Sample documents/New folder/Heat Merchants Ltd.pdf",
                1,
                [
                    HeaderList(1, "PRODUCT", [ItemCoordinate(45.09, 1075.74, 338.18, 1153.03)]),
                    HeaderList(2, "DESCRIPTION", [ItemCoordinate(338.18, 1078.96, 1317.29, 1156.25)]),
                    HeaderList(3, "QUANTITY", [ItemCoordinate(1320.51, 1075.74, 1655.48, 1153.03)]),
                    HeaderList(4, "PRICE", [ItemCoordinate(1658.70, 1072.51, 1987.22, 1149.81)]),
                    HeaderList(5, "VAT RATE", [ItemCoordinate(1987.22, 1078.96, 2090.28, 1153.03)]),
                    HeaderList(6, "VALUE", [ItemCoordinate(2099.94, 1078.96, 2370.49, 1146.59)]),
                ]
            ),
            PdfProperties(
                12,
                "Sample documents/New folder/Smiths Building Supplies.pdf",
                1,
                [
                    HeaderList(1, "PRODUCT", [ItemCoordinate(45.09, 1075.74, 338.18, 1153.03)]),
                    HeaderList(2, "DESCRIPTION", [ItemCoordinate(338.18, 1078.96, 1317.29, 1156.25)]),
                    HeaderList(3, "QUANTITY", [ItemCoordinate(1320.51, 1075.74, 1655.48, 1153.03)]),
                    HeaderList(4, "PRICE", [ItemCoordinate(1658.70, 1072.51, 1987.22, 1149.81)]),
                    HeaderList(5, "VAT RATE", [ItemCoordinate(1987.22, 1078.96, 2090.28, 1153.03)]),
                    HeaderList(6, "VALUE", [ItemCoordinate(2099.94, 1078.96, 2370.49, 1146.59)]),
                ]
            ),
            PdfProperties(
                13,
                "Sample documents/New folder/Premier Window board Ltd_.pdf",
                1,
                [
                    HeaderList(1, "Code", [ItemCoordinate(61.19, 785.87, 244.77, 858.84)]),
                    HeaderList(2, "Product Description", [ItemCoordinate(248, 782.64, 1391.37, 847.62)]),
                    HeaderList(3, "Quantity", [ItemCoordinate(1394.59, 785.87, 1623.27, 847.06)]),
                    HeaderList(4, "Price", [ItemCoordinate(1623.27, 779.42, 1861.61, 840.62)]),
                    HeaderList(5, "VAT Rate", [ItemCoordinate(1855.22, 776.20, 2096.72, 840.62)]),
                    HeaderList(6, "Net Amount", [ItemCoordinate(2096.72, 782.64, 2383.37, 847.06)]),
                ]
            ),
            PdfProperties(
                14,
                "Sample documents/New folder/SUB-CWI - Laois Attic & Wall Insulation Ltd_.pdf",
                1,
                [
                    HeaderList(1, "Code", [ItemCoordinate(106.28, 988.77, 447.68, 1075.74)]),
                    HeaderList(2, "Description", [ItemCoordinate(454.12, 992, 885.71, 1072.51)]),
                    HeaderList(3, "Quantity", [ItemCoordinate(888.93, 992, 1114.38, 1075.74)]),
                    HeaderList(4, "VAT Rate", [ItemCoordinate(1124.05, 992, 1339.84, 1069.29)]),
                    HeaderList(5, "Price", [ItemCoordinate(1343.06, 992, 1571.72, 1069.29)]),
                    HeaderList(6, "Discounted Price", [ItemCoordinate(1578.72, 992, 2054.85, 1069.29)]),
                    HeaderList(7, "Total", [ItemCoordinate(2141.72, 992, 2364.37, 1069.29)]),
                ]
            ),
            PdfProperties(
                15,
                "Sample documents/New folder/SUB-EWI - Ionut Sebastian Leoreanu.pdf",
                1,
                [
                    HeaderList(1, "QTY", [ItemCoordinate(199.68, 1188.46, 386.49, 1307.63)]),
                    HeaderList(2, "Description", [ItemCoordinate(405.81, 1198.12, 1410.70, 1307.63)]),
                    HeaderList(3, "UNIT PRICE", [ItemCoordinate(1420.36, 1198.12, 1903.38, 1301.19)]),
                    HeaderList(4, "AMOUNT", [ItemCoordinate(1916.36, 1198.12, 2302.84, 1301.19)]),
                ]
            ),
            PdfProperties(
                16,
                "Sample documents/New folder/SUB-EWI - Marcel Vircolici.pdf",
                1,
                [
                    HeaderList(1, "DESCRIPTION", [ItemCoordinate(115.90, 1457.14, 1533.31, 1589.61)]),
                    HeaderList(2, "RATE", [ItemCoordinate(1539.93, 1457.14, 2000.25, 1589.63)]),
                    HeaderList(3, "QTY", [ItemCoordinate(2010.19, 1460.45, 2189.02, 1596.23)]),
                    HeaderList(4, "AMOUNT", [ItemCoordinate(2192.33, 1453.83, 2437.10, 1589.61)]),
                ]
            ),
            PdfProperties(
                17,
                "Sample documents/New folder/SUB-H&P - Kevin O'Brien Heating & Plumbing Ltd_.pdf",
                4,
                [
                    HeaderList(1, "DESCRIPTION", [ItemCoordinate(96.66, 1727.49, 1269.49, 1781.80)]),
                    HeaderList(2, "QTY", [ItemCoordinate(1269.49, 1727.03, 1594.92, 1785.03)]),
                    HeaderList(3, "UNIT PRICE", [ItemCoordinate(1601.37, 1733.45, 1994.46, 1785.03)]),
                    HeaderList(4, "TOTAL", [ItemCoordinate(1994.46, 1727.03, 2394.10, 1788.25)]),
                ]
            ),
            PdfProperties(
                18,
                "Sample documents/New folder/SUB-H&P - Teeling Contracting Ltd_.pdf",
                1,
                [
                    HeaderList(1, "Qty", [ItemCoordinate(241.46, 1429.44, 347.70, 1500.27)]),
                    HeaderList(2, "Details", [ItemCoordinate(350.92, 1435.88, 1616.17, 1500.27)]),
                    HeaderList(3, "Unit Price", [ItemCoordinate(1619.39, 1429.45, 1802.90, 1497.03)]),
                    HeaderList(4, "Net", [ItemCoordinate(1802.90, 1432.66, 1947.78, 1500.27)]),
                    HeaderList(4, "Tax %", [ItemCoordinate(1947.78, 1432.66, 2095.88, 1497.05)]),
                    HeaderList(4, "Total", [ItemCoordinate(2095.88, 1429.44, 2260.10, 1497.25)]),
                ]
            ),
            PdfProperties(
                19,
                "Sample documents/New folder/Valentine Ladders.pdf",
                1,
                [
                    HeaderList(1, "Code", [ItemCoordinate(112.72, 1249.66, 354.28, 1343.06)]),
                    HeaderList(2, "Description", [ItemCoordinate(360.72, 1243.22, 1217.45, 1330.18)]),
                    HeaderList(3, "Qty", [ItemCoordinate(1223.89, 1246.45, 1384.90, 1333.40)]),
                    HeaderList(4, "Unit Price", [ItemCoordinate(1384.93, 1243.22, 1678.02, 1336.62)]),
                    HeaderList(4, "Disc", [ItemCoordinate(1681.24, 1243.22, 1813.29, 1336.62)]),
                    HeaderList(4, "Net Amt", [ItemCoordinate(1832.62, 1240.44, 2038.75, 1333.40)]),
                    HeaderList(4, "VAT %", [ItemCoordinate(2038.75, 1243.22, 2209.45, 1333.40)]),
                    HeaderList(4, "VAT", [ItemCoordinate(2212.67, 1249.66, 2360.83, 1339.84)]),
                ]
            ),
            PdfProperties(
                20,
                "Sample documents/New folder/Credit_Note_5973_from_Nationwide_Energy_Consultants.pdf",
                7,
                [
                    HeaderList(1, "DATE", [ItemCoordinate(135.77, 1341.23, 380.84, 1414.09)]),
                    HeaderList(2, "ACTIVITY", [ItemCoordinate(390.72, 1344.54, 831.23, 1417.40)]),
                    HeaderList(3, "DESCRIPTION", [ItemCoordinate(837.89, 1341.23, 1420.71, 1420.71)]),
                    HeaderList(4, "QTY", [ItemCoordinate(1460.45, 1344.54, 1718.76, 1420.71)]),
                    HeaderList(5, "TAX", [ItemCoordinate(1728.70, 1351.16, 1910.84, 1414.09)]),
                    HeaderList(6, "RATE", [ItemCoordinate(1914.15, 1351.16, 2116.16, 1420.71)]),
                    HeaderList(7, "AMOUNT", [ItemCoordinate(2149.28, 1344.54, 2457.27, 1417.40)])
                ]
            ),
            PdfProperties(
                21,
                "Sample documents/New folder/SUB-EWI - Mihai Grigoras.pdf",
                1,
                [
                    HeaderList(1, "DESCRIPTION", [
                        ItemCoordinate(22.53246753246754, 897.4675324675325, 1692.2727272727273, 1039.8701298701299)]),
                    HeaderList(2, "RATE", [ItemCoordinate(1850, 952, 1940, 980)]),
                    HeaderList(3, "QTY", [ItemCoordinate(2059, 952, 2134, 983)]),
                    HeaderList(4, "AMOUNT", [ItemCoordinate(2257, 952, 2424, 981)])
                ]
            ),
            PdfProperties(
                22,
                "Sample documents/New folder/C&F Quadrant Ltd.pdf",
                1,
                [
                    HeaderList(1, "Item", [ItemCoordinate(77, 1330, 152, 1357), ItemCoordinate(164, 1328, 247, 1357)]),
                    HeaderList(2, "Description", [ItemCoordinate(485, 1324, 674, 1368)]),
                    HeaderList(3, "Ordered", [ItemCoordinate(1041, 1328, 1179, 1357)]),
                    HeaderList(4, "Invoiced", [ItemCoordinate(1221, 1328, 1359, 1357)]),
                    HeaderList(5, "Unit Price €",
                               [ItemCoordinate(1434, 1329, 1503, 1357), ItemCoordinate(1515, 1329, 1595, 1357),
                                ItemCoordinate(1606, 1330, 1626, 1357)]),
                    HeaderList(6, "Disc %",
                               [ItemCoordinate(1718, 1329, 1784, 1358), ItemCoordinate(1794, 1329, 1822, 1358)]),
                    HeaderList(7, "VAT", [ItemCoordinate(1955, 1330, 2024, 1357)]),
                    HeaderList(8, "Total Inc VAT €",
                               [ItemCoordinate(2117, 1328, 2201, 1357), ItemCoordinate(2214, 1330, 2261, 1357),
                                ItemCoordinate(2271, 1330, 2340, 1357), ItemCoordinate(2349, 1330, 2369, 1357)])
                ]
            ),
            PdfProperties(
                23,
                "Sample documents/New folder/Chadwicks CN.pdf",
                1,
                [
                    HeaderList(6, "ITEM", [ItemCoordinate(109, 1348, 188, 1389)]),
                    HeaderList(7, "QTY", [ItemCoordinate(287, 1352, 358, 1380)]),
                    HeaderList(8, "UNIT", [ItemCoordinate(459, 1352, 538, 1378)]),
                    HeaderList(9, "DESCRIPTION", [ItemCoordinate(620, 1348, 857, 1389)]),
                    HeaderList(1, "UNIT EXCL. VAT",
                               [ItemCoordinate(1609, 1308, 1681, 1348), ItemCoordinate(1609, 1352, 1708, 1378),
                                ItemCoordinate(1721, 1352, 1791, 1378)]),
                    HeaderList(2, "TOTAL EXCL. VAT",
                               [ItemCoordinate(1851, 1304, 1957, 1344), ItemCoordinate(1853, 1352, 1952, 1378),
                                ItemCoordinate(1964, 1352, 2034, 1378)]),
                    HeaderList(3, "TOTAL INCL.VAT",
                               [ItemCoordinate(2088, 1303, 2195, 1343), ItemCoordinate(2086, 1352, 2252, 1378)]),
                    HeaderList(4, "VAT CODE",
                               [ItemCoordinate(2312, 1312, 2377, 1338), ItemCoordinate(2314, 1355, 2413, 1381)])
                ]
            ),
            PdfProperties(
                24,
                "Sample documents/New folder/ExtraClean Contract Cleaners.pdf",
                4,
                [
                    HeaderList(1, "Hours", [
                        ItemCoordinate(410.64935064935065, 1013.3766233766235, 642.4675324675325, 1099.4805194805197)]),
                    HeaderList(2, "Description of services", [
                        ItemCoordinate(665.6493506493507, 1026.6233766233765, 1268.3766233766235, 1106.103896103896)]),
                    HeaderList(3, "Price per hour", [
                        ItemCoordinate(1281.6233766233768, 1026.6233766233765, 2086.3636363636365, 1096.168831168831)]),
                    HeaderList(4, "Total", [
                        ItemCoordinate(2122.792207792208, 1023.3116883116884, 2295.0000000000005, 1106.1038961038962)])
                ]
            ),
            PdfProperties(
                25,
                "Sample documents/New folder/FSW.pdf",
                1,
                [
                    HeaderList(1, "Stock Code",
                               [ItemCoordinate(144, 1238, 235, 1267), ItemCoordinate(248, 1238, 334, 1267)]),
                    HeaderList(2, "Description", [ItemCoordinate(499, 1234, 681, 1279)]),
                    HeaderList(3, "Qty", [ItemCoordinate(1348, 1238, 1404, 1274)]),
                    HeaderList(4, "Vat", [ItemCoordinate(1461, 1239, 1516, 1267)]),
                    HeaderList(5, "Unit Price", [
                        ItemCoordinate(1536.9311688311689, 1211.5012987012988, 1833.3623376623377, 1285.609090909091)]),
                    HeaderList(6, "Disc", [ItemCoordinate(1830.1402597402598, 1224.3896103896104, 2004.1324675324677,
                                                          1269.4987012987012)]),
                    HeaderList(7, "EUR Total", [
                        ItemCoordinate(1997.6883116883116, 1211.5012987012988, 2326.3402597402596, 1282.3870129870131)])
                ]
            ),
            PdfProperties(
                26,
                "Sample documents/New folder/PF 2 Page.pdf",
                1,
                [
                    HeaderList(1, "Item", [ItemCoordinate(150, 1097, 216, 1121)]),
                    HeaderList(2, "Name", [ItemCoordinate(400, 1097, 493, 1121)]),
                    HeaderList(3, "Quantity", [ItemCoordinate(1774, 1093, 1910, 1132)]),
                    HeaderList(4, "Price", [ItemCoordinate(2027, 1097, 2100, 1121)]),
                    HeaderList(5, "Total", [ItemCoordinate(2206, 1096, 2286, 1121)])
                ]
            ),
            PdfProperties(
                27,
                "Sample documents/New folder/SUB-EWI - Petru Ghereben.pdf",
                2,
                [
                    HeaderList(1, "DESCRIPTION", [ItemCoordinate(265, 956, 517, 1004)]),
                    HeaderList(2, "AMOUNT", [ItemCoordinate(2041, 956, 2208, 1004)])
                ]
            ),
            PdfProperties(
                28,
                "Sample documents/New folder/SUB-EWI - Sorin Ionel Mitrea.pdf",
                2,
                [
                    HeaderList(1, "QTY", [ItemCoordinate(248, 1094, 322, 1144)]),
                    HeaderList(2, "DESCRIPTION", [
                        ItemCoordinate(380.0519480519481, 1056.4155844155844, 1375.2727272727275, 1172.3636363636363)]),
                    HeaderList(3, "UNIT PRICE",
                               [ItemCoordinate(1511, 1094, 1599, 1142), ItemCoordinate(1613, 1094, 1724, 1141)]),
                    HeaderList(4, "AMOUNT", [ItemCoordinate(2098, 1094, 2265, 1142)])
                ]
            ),
            PdfProperties(
                29,
                "Sample documents/New folder/Airpacks Ltd CN.pdf",
                7,
                [
                    HeaderList(1, "Item Code", [
                        ItemCoordinate(123.82077922077922, 1609.6701298701298, 488.76623376623377,
                                       1681.3558441558441)]),
                    HeaderList(2, "Description", [
                        ItemCoordinate(492.0246753246753, 1603.1532467532465, 1518.4337662337662, 1681.355844155844)]),
                    HeaderList(3, "Qty", [ItemCoordinate(1528.2090909090907, 1606.4116883116883, 1792.1428571428569,
                                                         1684.6142857142856)]),
                    HeaderList(4, "Unit Price", [
                        ItemCoordinate(1801.9181818181817, 1596.6363636363635, 2062.5935064935065,
                                       1681.3558441558441)]),
                    HeaderList(5, "Total", [
                        ItemCoordinate(2065.851948051948, 1606.4116883116883, 2368.887012987013, 1674.838961038961)])
                ]
            ),
            PdfProperties(
                30,
                "Sample documents/New folder/Airpacks Ltd.pdf",
                1,
                [
                    HeaderList(1, "Item Code", [
                        ItemCoordinate(93.40, 1668.36, 489.55, 1732.77)]),
                    HeaderList(2, "Description", [
                        ItemCoordinate(531.42, 1674.80, 1507.32, 1729.55)]),
                    HeaderList(3, "Qty", [ItemCoordinate(1526.6493506493507, 1674.80, 1681.24,
                                                         1736.0000000000002)]),
                    HeaderList(4, "Unit", [
                        ItemCoordinate(1713.45, 1678.02, 1871.27, 1736)]),
                    HeaderList(5, "Unit Price", [
                        ItemCoordinate(1926.02, 1678.02, 2154.70, 1736)]),
                    HeaderList(6, "Total", [
                        ItemCoordinate(2174, 1674, 2367, 1732)])
                ]
            ),
            PdfProperties(
                31,
                "Sample documents/New folder/Alan Bardon Motors Ltd.pdf",
                1,
                [
                    HeaderList(1, "Parts", [
                        ItemCoordinate(135.27272727272728, 1275.4285714285716, 260.8831168831169, 1343.0649350649353)]),
                    HeaderList(2, "Description", [
                        ItemCoordinate(309.1948051948052, 1240, 1442.909090909091, 1330.1818181818182)])
                ]
            ),
            PdfProperties(
                32,
                "Sample documents/New folder/Aurivo Limited.pdf",
                1,
                [
                    HeaderList(1, "PRODUCT", [
                        ItemCoordinate(48.311688311688314, 1075.7402597402597, 334.961038961039, 1146.5974025974026)]),
                    HeaderList(2, "DESCRIPTION", [
                        ItemCoordinate(334.961038961039, 1072.5194805194806, 1304.4155844155844, 1149.818181818182)]),
                    HeaderList(3, "QUANTITY", [
                        ItemCoordinate(1326.961038961039, 1075.7402597402597, 1652.2597402597403, 1149.8181818181818)]),
                    HeaderList(4, "PRICE", [
                        ItemCoordinate(1665.1428571428573, 1075.7402597402597, 1977.5584415584417,
                                       1162.7012987012986)]),
                    HeaderList(5, "VALUE", [
                        ItemCoordinate(2096.727272727273, 1072.5194805194806, 2370.4935064935066, 1149.818181818182)])
                ]
            ),
            PdfProperties(
                33,
                "Sample documents/New folder/C&F Quadrant Ltd CN.pdf",
                1,
                [
                    HeaderList(1, "Item Code", [
                        ItemCoordinate(67.63636363636364, 1320.5194805194806, 402.5974025974026, 1375.2727272727273)]),
                    HeaderList(2, "Description", [
                        ItemCoordinate(421.92207792207796, 1320.5194805194806, 1004.8831168831169, 1372.051948051948)]),
                    HeaderList(3, "Ordered",
                               [ItemCoordinate(1008.1038961038962, 1320.5194805194806, 1240, 1381.7142857142858)]),
                    HeaderList(4, "Invoiced", [
                        ItemCoordinate(1236.7792207792209, 1317.2987012987014, 1442.909090909091, 1378.4935064935066)]),
                    HeaderList(5, "Unit Price €", [ItemCoordinate(1434, 1329, 1503, 1357),
                                                   ItemCoordinate(1446.1298701298701, 1320.5194805194806,
                                                                  1716.6753246753246, 1378.4935064935066)]),
                    HeaderList(6, "Disc %", [
                        ItemCoordinate(1716.6753246753249, 1310.857142857143, 1916.3636363636365, 1381.7142857142858)]),
                    HeaderList(7, "VAT", [
                        ItemCoordinate(1919.5844155844156, 1317.2987012987014, 2087.064935064935, 1375.2727272727275)]),
                    HeaderList(8, "Total Inc VAT €", [
                        ItemCoordinate(2103.1688311688313, 1320.5194805194806, 2370.4935064935066, 1381.7142857142858)])
                ]
            ),
            PdfProperties(
                34,
                "Sample documents/New folder/Chadwicks 1 Page.pdf",
                1,
                [
                    HeaderList(1, "ITEM", [ItemCoordinate(67.0, 1285, 238, 1398)]),
                    HeaderList(2, "QTY", [ItemCoordinate(244, 1285, 412, 1401)]),
                    HeaderList(3, "UNIT", [ItemCoordinate(422, 1285, 586, 1395)]),
                    HeaderList(4, "DESCRIPTION", [ItemCoordinate(589, 1285, 1598, 1391)]),
                    HeaderList(5, "EXCL. VAT", [ItemCoordinate(1601, 1285, 1833, 1391)]),
                    HeaderList(6, "EXCL. VAT", [ItemCoordinate(1836, 1282, 2071, 1395)]),
                    HeaderList(7, "INCL.VAT", [ItemCoordinate(2075, 1282, 2300, 1398)]),
                    HeaderList(8, "CODE", [ItemCoordinate(2303, 1288, 2423, 1398)])
                ]
            ), PdfProperties(
                35,
                "Sample documents/New folder/Davies Limited CN.pdf",
                1,
                [
                    HeaderList(1, "ITEM", [ItemCoordinate(67.0, 1285, 238, 1398)]),
                    HeaderList(2, "QTY", [ItemCoordinate(244, 1285, 412, 1401)]),
                    HeaderList(3, "UNIT", [ItemCoordinate(422, 1285, 586, 1395)]),
                    HeaderList(4, "DESCRIPTION", [ItemCoordinate(589, 1285, 1598, 1391)]),
                    HeaderList(5, "EXCL. VAT", [ItemCoordinate(1601, 1285, 1833, 1391)]),
                    HeaderList(6, "EXCL. VAT", [ItemCoordinate(1836, 1282, 2071, 1395)]),
                    HeaderList(7, "INCL.VAT", [ItemCoordinate(2075, 1282, 2300, 1398)]),
                    HeaderList(8, "CODE", [ItemCoordinate(2303, 1288, 2423, 1398)])
                ]
            ), PdfProperties(
                36,
                "Sample documents/New folder/Davies Limited.pdf",
                1,
                [
                    HeaderList(1, "ITEM", [ItemCoordinate(67.0, 1285, 238, 1398)]),
                    HeaderList(2, "QTY", [ItemCoordinate(244, 1285, 412, 1401)]),
                    HeaderList(3, "UNIT", [ItemCoordinate(422, 1285, 586, 1395)]),
                    HeaderList(4, "DESCRIPTION", [ItemCoordinate(589, 1285, 1598, 1391)]),
                    HeaderList(5, "EXCL. VAT", [ItemCoordinate(1601, 1285, 1833, 1391)]),
                    HeaderList(6, "EXCL. VAT", [ItemCoordinate(1836, 1282, 2071, 1395)]),
                    HeaderList(7, "INCL.VAT", [ItemCoordinate(2075, 1282, 2300, 1398)]),
                    HeaderList(8, "CODE", [ItemCoordinate(2303, 1288, 2423, 1398)])
                ]
            ), PdfProperties(
                37,
                "Sample documents/New folder/E&G Insulation.pdf",
                1,
                [
                    HeaderList(1, "DESCRIPTION", [
                        ItemCoordinate(225.45454545454547, 1072.5194805194806, 1990.4285714285716,
                                       1185.2467532467533)]),
                    HeaderList(2, "AMOUNT", [
                        ItemCoordinate(2016.2077922077924, 1066.077922077922, 2341.506493506494, 1185.2467532467533)])
                ]
            ), PdfProperties(
                38,
                "Sample documents/New folder/Harlow Agencies Limited CN.pdf",
                1,
                [
                    HeaderList(1, "Item Code", [
                        ItemCoordinate(75.5248344370861, 1063.1572847682119, 499.62582781456956, 1138.682119205298)]),
                    HeaderList(2, "Description", [ItemCoordinate(505, 1070, 1572, 1121)]),
                    HeaderList(3, "Quantity", [ItemCoordinate(1567, 1061, 1850.2, 1125.61)]),
                    HeaderList(4, "UOM", [ItemCoordinate(1854, 1061, 2150, 1134)]),
                    HeaderList(5, "Unit Price", [ItemCoordinate(2155, 1057, 2460, 1130)]),
                    HeaderList(6, "Amount", [ItemCoordinate(2469, 1061, 2807, 1134)]),
                    HeaderList(7, "Dis %", [ItemCoordinate(2816, 1061, 3030, 1134)]),
                    HeaderList(8, "Line Total", [ItemCoordinate(3044, 1070, 3349.5, 1130)])
                ]
            ), PdfProperties(
                39,
                "Sample documents/New folder/Hevac Limited.pdf",
                1,
                [
                    HeaderList(1, "Quantity", [
                        ItemCoordinate(112.77272727272728, 1466.0454545454545, 441.4246753246754, 1527.2649350649351)]),
                    HeaderList(2, "Product", [
                        ItemCoordinate(451.0909090909091, 1462.8233766233766, 1437.0467532467533, 1527.2649350649351)]),
                    HeaderList(3, "Price", [ItemCoordinate(1478.9337662337662, 1462.8233766233766, 1975.1337662337662,
                                                           1527.2649350649351)]),
                    HeaderList(4, "Total V", [
                        ItemCoordinate(2013.7987012987014, 1462.8233766233766, 2355.3389610389613, 1527.2649350649351)])
                ]
            ), PdfProperties(
                40,
                "Sample documents/New folder/Hilti - Long Term Rentals (DD) CN.pdf",
                1,
                [
                    HeaderList(1, "Item No.", [
                        ItemCoordinate(225.54545454545456, 1424.1584415584416, 428.53636363636366, 1578.818181818182)]),
                    HeaderList(2, "Description", [
                        ItemCoordinate(428.53636363636366, 1430.6025974025974, 1034.287012987013, 1578.818181818182)]),
                    HeaderList(3, "Serial Number", [
                        ItemCoordinate(1037.509090909091, 1427.3805194805195, 1340.3844155844156, 1582.04025974026)]),
                    HeaderList(4, "Start Date", [
                        ItemCoordinate(1343.6064935064935, 1427.3805194805195, 1794.6974025974027, 1575.596103896104)]),
                    HeaderList(5, "Monthly Rate Per Unit", [
                        ItemCoordinate(1801.1415584415583, 1420.9363636363637, 2136.237662337662, 1578.818181818182)]),
                    HeaderList(6, "Total", [
                        ItemCoordinate(2139.45974025974, 1427.3805194805195, 2397.2259740259738, 1578.818181818182)])
                ]
            ), PdfProperties(
                41,
                "Sample documents/New folder/Hilti - Long Term Rentals (DD).pdf",
                1,
                [
                    HeaderList(1, "Item No.", [
                        ItemCoordinate(231.9896103896104, 1382.2714285714285, 438.2025974025974, 1453.1571428571428)]),
                    HeaderList(2, "Description", [
                        ItemCoordinate(441.4246753246753, 1388.7155844155843, 1346.8285714285714, 1456.3792207792208)]),
                    HeaderList(3, "Qty", [ItemCoordinate(1369.3831168831168, 1391.9376623376625, 1478.9337662337662,
                                                         1449.9350649350652)]),
                    HeaderList(4, "Unit", [
                        ItemCoordinate(1536.9311688311689, 1388.7155844155843, 1698.0350649350648, 1446.712987012987)]),
                    HeaderList(5, "Unit Price", [
                        ItemCoordinate(1756.0324675324675, 1382.2714285714285, 1975.1337662337662, 1446.712987012987)]),
                    HeaderList(6, "Item Value", [
                        ItemCoordinate(2158.7922077922076, 1382.2714285714285, 2361.7831168831167, 1446.712987012987)])
                ]
            ), PdfProperties(
                42,
                "Sample documents/New folder/IConstruction Products Ltd.pdf",
                1,
                [
                    HeaderList(1, "Quantity", [
                        ItemCoordinate(138.49350649350652, 1236.7792207792209, 338.18181818181824,
                                       1314.0779220779223)]),
                    HeaderList(2, "Details",
                               [ItemCoordinate(341.4025974025974, 1246.4415584415585, 1240, 1310.857142857143)]),
                    HeaderList(3, "Unit Price",
                               [ItemCoordinate(1240, 1252.883116883117, 1516.987012987013, 1314.0779220779223)]),
                    HeaderList(4, "Disc Rate", [
                        ItemCoordinate(1516.987012987013, 1256.1038961038962, 1819.7402597402597, 1307.6363636363637)]),
                    HeaderList(5, "Net", [
                        ItemCoordinate(1826.1818181818182, 1252.883116883117, 1971.1168831168832, 1310.8571428571431)]),
                    HeaderList(6, "Vat %", [
                        ItemCoordinate(1974.3376623376626, 1252.883116883117, 2174.0259740259744, 1320.5194805194808)]),
                    HeaderList(7, "Vat", [
                        ItemCoordinate(2186.909090909091, 1249.6623376623377, 2322.1818181818185, 1320.5194805194806)])
                ]
            ), PdfProperties(
                43,
                "Sample documents/New folder/Liam Cawley Hardware.pdf",
                6,
                [
                    HeaderList(1, "Item Code", [
                        ItemCoordinate(70.85714285714286, 1175.5844155844156, 376.83116883116884, 1246.4415584415585)]),
                    HeaderList(2, "Batch", [
                        ItemCoordinate(376.83116883116884, 1178.8051948051948, 628.0519480519481, 1252.8831168831168)]),
                    HeaderList(3, "Description", [
                        ItemCoordinate(634.4935064935065, 1175.5844155844156, 1394.5974025974028, 1246.4415584415585)]),
                    HeaderList(4, "Quantity", [
                        ItemCoordinate(1401.0389610389611, 1178.8051948051948, 1729.5584415584417,
                                       1249.6623376623377)]),
                    HeaderList(5, "Unit Price",
                               [ItemCoordinate(1736, 1175.5844155844156, 2038.753246753247, 1249.6623376623377)]),
                    HeaderList(6, "Amount", [
                        ItemCoordinate(2054.857142857143, 1172.3636363636365, 2380.1558441558445, 1249.662337662338)])
                ]
            ), PdfProperties(
                44,
                "Sample documents/New folder/McGrath Ind Waste Ltd_.pdf",
                1,
                [
                    HeaderList(1, "Date", [
                        ItemCoordinate(61.1948051948052, 1085.4025974025974, 225.4545454545455, 1124.051948051948)]),
                    HeaderList(2, "Job ID", [
                        ItemCoordinate(221.72185430463574, 1088.0794701986754, 336.6887417218543, 1125.0331125827813)]),
                    HeaderList(3, "PON", [
                        ItemCoordinate(340.79470198675494, 1083.9735099337747, 427.01986754966885, 1129.139072847682)]),
                    HeaderList(4, "Order Type", [
                        ItemCoordinate(427.01986754966885, 1088.0794701986754, 636.4238410596026, 1129.139072847682)]),
                    HeaderList(5, "Site Name", [
                        ItemCoordinate(640.5298013245033, 1083.9735099337747, 837.615894039735, 1129.139072847682)]),
                    HeaderList(6, "Description", [
                        ItemCoordinate(837.615894039735, 1083.9735099337747, 1839.4701986754967, 1125.0331125827813)]),
                    HeaderList(7, "Qty", [ItemCoordinate(1839.4701986754965, 1088.0794701986754, 1913.3774834437083,
                                                         1125.0331125827813)]),
                    HeaderList(8, "VAT", [
                        ItemCoordinate(1917.483443708609, 1083.9735099337747, 2098.1456953642382, 1120.9271523178807)]),
                    HeaderList(9, "Price", [
                        ItemCoordinate(2098.1456953642382, 1088.0794701986754, 2291.125827814569, 1125.0331125827813)]),
                    HeaderList(10, "Total", [
                        ItemCoordinate(2287.0198675496686, 1083.9735099337747, 2414.304635761589, 1125.0331125827813)]),
                ]
            ), PdfProperties(
                45,
                "Sample documents/New folder/North Mayo Construction & Hire.pdf",
                1,
                [
                    HeaderList(1, "Code", [
                        ItemCoordinate(123.17880794701986, 1219.4701986754965, 377.7483443708609, 1289.2715231788077)]),
                    HeaderList(2, "Description", [
                        ItemCoordinate(385.9602649006622, 1219.4701986754965, 1120.9271523178807, 1289.2715231788077)]),
                    HeaderList(3, "Time Chg", [
                        ItemCoordinate(1120.9271523178807, 1219.4701986754965, 1465.8278145695363, 1285.165562913907)]),
                    HeaderList(4, "Qty", [
                        ItemCoordinate(1465.8278145695363, 1219.4701986754965, 1597.2185430463574, 1285.165562913907)]),
                    HeaderList(5, "Unit Price", [
                        ItemCoordinate(1601.3245033112582, 1219.4701986754965, 1843.5761589403974, 1285.165562913907)]),
                    HeaderList(6, "Vat", [
                        ItemCoordinate(1847.6821192052978, 1223.5761589403971, 2024.2384105960264, 1285.165562913907)]),
                    HeaderList(7, "Disc", [
                        ItemCoordinate(2032.4503311258277, 1223.5761589403971, 2209.006622516556, 1285.165562913907)]),
                    HeaderList(8, "Value", [
                        ItemCoordinate(2209.006622516556, 1223.5761589403971, 2360.9271523178804, 1289.2715231788077)])
                ]
            )
        ]
        pass

    def find_by_id(self, index):
        return self.collection[index - 1]
