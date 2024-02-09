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
                ]
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
                    HeaderList(1, "Code", [ItemCoordinate(61.19, 785.87, 244.77, 843.84)]),
                    HeaderList(2, "Product Description", [ItemCoordinate(248, 782.64, 1391.37, 840.62)]),
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
        ]
        pass

    def find_by_id(self, index):
        return self.collection[index - 1]
