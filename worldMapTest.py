# worldMapTest.py
import pygal
import csv



# output to a csv file
def outputCsv(filename, listOfList):
    with open(filename, 'wb') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(listOfList)

# SHORT_COUNTRY = [['ad', 'Andorra'], ['ae', 'United Arab Emirates'], ['af', 'Afghanistan'], ['al', 'Albania'], ['am', 'Armenia'], ['ao', 'Angola'], ['aq', 'Antarctica'], ['ar', 'Argentina'], ['at', 'Austria'], ['au', 'Australia'], ['az', 'Azerbaijan'], ['ba', 'Bosnia and Herzegovina'], ['bd', 'Bangladesh'], ['be', 'Belgium'], ['bf', 'Burkina Faso'], ['bg', 'Bulgaria'], ['bh', 'Bahrain'], ['bi', 'Burundi'], ['bj', 'Benin'], ['bn', 'Brunei Darussalam'], ['bo', 'Bolivia, Plurinational State of'], ['br', 'Brazil'], ['bt', 'Bhutan'], ['bw', 'Botswana'], ['by', 'Belarus'], ['bz', 'Belize'], ['ca', 'Canada'], ['cd', 'Congo, the Democratic Republic of the'], ['cf', 'Central African Republic'], ['cg', 'Congo'], ['ch', 'Switzerland'], ['ci', 'Cote d\xd5Ivoire'], ['cl', 'Chile'], ['cm', 'Cameroon'], ['cn', 'China'], ['co', 'Colombia'], ['cr', 'Costa Rica'], ['cu', 'Cuba'], ['cv', 'Cape Verde'], ['cy', 'Cyprus'], ['cz', 'Czech Republic'], ['de', 'Germany'], ['dj', 'Djibouti'], ['dk', 'Denmark'], ['do', 'Dominican Republic'], ['dz', 'Algeria'], ['ec', 'Ecuador'], ['ee', 'Estonia'], ['eg', 'Egypt'], ['eh', 'Western Sahara'], ['er', 'Eritrea'], ['es', 'Spain'], ['et', 'Ethiopia'], ['fi', 'Finland'], ['fr', 'France'], ['ga', 'Gabon'], ['gb', 'United Kingdom'], ['ge', 'Georgia'], ['gf', 'French Guiana'], ['gh', 'Ghana'], ['gl', 'Greenland'], ['gm', 'Gambia'], ['gn', 'Guinea'], ['gq', 'Equatorial Guinea'], ['gr', 'Greece'], ['gt', 'Guatemala'], ['gu', 'Guam'], ['gw', 'Guinea-Bissau'], ['gy', 'Guyana'], ['hk', 'Hong Kong'], ['hn', 'Honduras'], ['hr', 'Croatia'], ['ht', 'Haiti'], ['hu', 'Hungary'], ['id', 'Indonesia'], ['ie', 'Ireland'], ['il', 'Israel'], ['in', 'India'], ['iq', 'Iraq'], ['ir', 'Iran, Islamic Republic of'], ['is', 'Iceland'], ['it', 'Italy'], ['jm', 'Jamaica'], ['jo', 'Jordan'], ['jp', 'Japan'], ['ke', 'Kenya'], ['kg', 'Kyrgyzstan'], ['kh', 'Cambodia'], ['kp', 'Korea, Democratic People\xd5s Republic of'], ['kr', 'Korea, Republic of'], ['kw', 'Kuwait'], ['kz', 'Kazakhstan'], ['la', 'Lao People\xd5s Democratic Republic'], ['lb', 'Lebanon'], ['li', 'Liechtenstein'], ['lk', 'Sri Lanka'], ['lr', 'Liberia'], ['ls', 'Lesotho'], ['lt', 'Lithuania'], ['lu', 'Luxembourg'], ['lv', 'Latvia'], ['ly', 'Libyan Arab Jamahiriya'], ['ma', 'Morocco'], ['mc', 'Monaco'], ['md', 'Moldova, Republic of'], ['me', 'Montenegro'], ['mg', 'Madagascar'], ['mk', 'Macedonia, the former Yugoslav Republic of'], ['ml', 'Mali'], ['mm', 'Myanmar'], ['mn', 'Mongolia'], ['mo', 'Macao'], ['mr', 'Mauritania'], ['mt', 'Malta'], ['mu', 'Mauritius'], ['mv', 'Maldives'], ['mw', 'Malawi'], ['mx', 'Mexico'], ['my', 'Malaysia'], ['mz', 'Mozambique'], ['na', 'Namibia'], ['ne', 'Niger'], ['ng', 'Nigeria'], ['ni', 'Nicaragua'], ['nl', 'Netherlands'], ['no', 'Norway'], ['np', 'Nepal'], ['nz', 'New Zealand'], ['om', 'Oman'], ['pa', 'Panama'], ['pe', 'Peru'], ['pg', 'Papua New Guinea'], ['ph', 'Philippines'], ['pk', 'Pakistan'], ['pl', 'Poland'], ['pr', 'Puerto Rico'], ['ps', 'Palestine, State of'], ['pt', 'Portugal'], ['py', 'Paraguay'], ['re', 'Reunion'], ['ro', 'Romania'], ['rs', 'Serbia'], ['ru', 'Russian Federation'], ['rw', 'Rwanda'], ['sa', 'Saudi Arabia'], ['sc', 'Seychelles'], ['sd', 'Sudan'], ['se', 'Sweden'], ['sg', 'Singapore'], ['sh', 'Saint Helena, Ascension and Tristan da Cunha'], ['si', 'Slovenia'], ['sk', 'Slovakia'], ['sl', 'Sierra Leone'], ['sm', 'San Marino'], ['sn', 'Senegal'], ['so', 'Somalia'], ['sr', 'Suriname'], ['st', 'Sao Tome and Principe'], ['sv', 'El Salvador'], ['sy', 'Syrian Arab Republic'], ['sz', 'Swaziland'], ['td', 'Chad'], ['tg', 'Togo'], ['th', 'Thailand'], ['tj', 'Tajikistan'], ['tl', 'Timor-Leste'], ['tm', 'Turkmenistan'], ['tn', 'Tunisia'], ['tr', 'Turkey'], ['tw', 'Taiwan, Province of China'], ['tz', 'Tanzania, United Republic of'], ['ua', 'Ukraine'], ['ug', 'Uganda'], ['us', 'United States'], ['uy', 'Uruguay'], ['uz', 'Uzbekistan'], ['va', 'Holy See (Vatican City State)'], ['ve', 'Venezuela, Bolivarian Republic of'], ['vn', 'Viet Nam'], ['ye', 'Yemen'], ['yt', 'Mayotte'], ['za', 'South Africa'], ['zm', 'Zambia'], ['zw', 'Zimbabwe']]
#
# with open('./output/queries/q1_4.csv', 'rb') as csvfile:
#     country_count = list(csv.reader(csvfile))
# # find the abbreviation for each country
# for row in country_count[1:]:
#     ori_ctryName = row[0]
#     for mapRow in SHORT_COUNTRY:
#         if (ori_ctryName in mapRow[1].upper()):
#             row.append(mapRow[0])
# # mannally add abbreviation for those don't have a match
# for row in country_count[1:]:
#     if (row[0] == 'SOUTH KOREA'):
#         row.append('kr')
#     elif (row[0] == 'BURMA (MYANMAR)'):
#         row.append('mm')
#     elif (row[0] == 'MACAU'):
#         row.append('mo')
#     elif (row[0] == 'SERBIA AND MONTENEGRO'):
#         row.append('rs')
#     elif (row[0] == 'VIETNAM'):
#         row.append('vn')
#     elif (row[0] == 'PALESTINIAN TERRITORIES'):
#         row.append('ps')
# # delete those countries without a specified abbreviation
# # adjust those countries has more than one abbreviations
# for row in country_count[1:]:
#     if (len(row) < 3 or row[0] == ''):
#         country_count.remove(row)
#     elif (row[0] in ['CHINA', 'NIGER', 'GUINEA']):
#         country_count.append(row[:3])
#         country_count.remove(row)
# # replace the FullName with the abbreviations
# country_count[0].append('abbrCountryName')
# country_count = [[x[2],x[1]] for x in country_count]
# # sort by count
# titileRow = country_count[0]
# del country_count[0]
# country_count.sort(key=lambda x: int(x[1]), reverse=True)
# country_count.insert(0, titileRow)

# for each in country_count:
#     print each


ABBR_FULLNAME = [['AFG', 'Afghanistan'], ['ALB', 'Albania'], ['DZA', 'Algeria'], ['ASM', 'American Samoa'], ['AND', 'Andorra'], ['AGO', 'Angola'], ['AIA', 'Anguilla'], ['ATG', 'Antigua and Barbuda'], ['ARG', 'Argentina'], ['ARM', 'Armenia'], ['ABW', 'Aruba'], ['AUS', 'Australia'], ['AUT', 'Austria'], ['AZE', 'Azerbaijan'], ['BHM', 'Bahamas, The'], ['BHR', 'Bahrain'], ['BGD', 'Bangladesh'], ['BRB', 'Barbados'], ['BLR', 'Belarus'], ['BEL', 'Belgium'], ['BLZ', 'Belize'], ['BEN', 'Benin'], ['BMU', 'Bermuda'], ['BTN', 'Bhutan'], ['BOL', 'Bolivia'], ['BIH', 'Bosnia and Herzegovina'], ['BWA', 'Botswana'], ['BRA', 'Brazil'], ['VGB', 'British Virgin Islands'], ['BRN', 'Brunei'], ['BGR', 'Bulgaria'], ['BFA', 'Burkina Faso'], ['MMR', 'Burma'], ['BDI', 'Burundi'], ['CPV', 'Cabo Verde'], ['KHM', 'Cambodia'], ['CMR', 'Cameroon'], ['CAN', 'Canada'], ['CYM', 'Cayman Islands'], ['CAF', 'Central African Republic'], ['TCD', 'Chad'], ['CHL', 'Chile'], ['CHN', 'China'], ['COL', 'Colombia'], ['COM', 'Comoros'], ['COD', 'Congo, Democratic Republic of the'], ['COG', 'Congo, Republic of the'], ['COK', 'Cook Islands'], ['CRI', 'Costa Rica'], ['CIV', "Cote d'Ivoire"], ['HRV', 'Croatia'], ['CUB', 'Cuba'], ['CUW', 'Curacao'], ['CYP', 'Cyprus'], ['CZE', 'Czech Republic'], ['DNK', 'Denmark'], ['DJI', 'Djibouti'], ['DMA', 'Dominica'], ['DOM', 'Dominican Republic'], ['ECU', 'Ecuador'], ['EGY', 'Egypt'], ['SLV', 'El Salvador'], ['GNQ', 'Equatorial Guinea'], ['ERI', 'Eritrea'], ['EST', 'Estonia'], ['ETH', 'Ethiopia'], ['FLK', 'Falkland Islands (Islas Malvinas)'], ['FRO', 'Faroe Islands'], ['FJI', 'Fiji'], ['FIN', 'Finland'], ['FRA', 'France'], ['PYF', 'French Polynesia'], ['GAB', 'Gabon'], ['GMB', 'Gambia, The'], ['GEO', 'Georgia'], ['DEU', 'Germany'], ['GHA', 'Ghana'], ['GIB', 'Gibraltar'], ['GRC', 'Greece'], ['GRL', 'Greenland'], ['GRD', 'Grenada'], ['GUM', 'Guam'], ['GTM', 'Guatemala'], ['GGY', 'Guernsey'], ['GNB', 'Guinea-Bissau'], ['GIN', 'Guinea'], ['GUY', 'Guyana'], ['HTI', 'Haiti'], ['HND', 'Honduras'], ['HKG', 'Hong Kong'], ['HUN', 'Hungary'], ['ISL', 'Iceland'], ['IND', 'India'], ['IDN', 'Indonesia'], ['IRN', 'Iran'], ['IRQ', 'Iraq'], ['IRL', 'Ireland'], ['IMN', 'Isle of Man'], ['ISR', 'Israel'], ['ITA', 'Italy'], ['JAM', 'Jamaica'], ['JPN', 'Japan'], ['JEY', 'Jersey'], ['JOR', 'Jordan'], ['KAZ', 'Kazakhstan'], ['KEN', 'Kenya'], ['KIR', 'Kiribati'], ['KOR', 'Korea, North'], ['PRK', 'Korea, South'], ['KSV', 'Kosovo'], ['KWT', 'Kuwait'], ['KGZ', 'Kyrgyzstan'], ['LAO', 'Laos'], ['LVA', 'Latvia'], ['LBN', 'Lebanon'], ['LSO', 'Lesotho'], ['LBR', 'Liberia'], ['LBY', 'Libya'], ['LIE', 'Liechtenstein'], ['LTU', 'Lithuania'], ['LUX', 'Luxembourg'], ['MAC', 'Macau'], ['MKD', 'Macedonia'], ['MDG', 'Madagascar'], ['MWI', 'Malawi'], ['MYS', 'Malaysia'], ['MDV', 'Maldives'], ['MLI', 'Mali'], ['MLT', 'Malta'], ['MHL', 'Marshall Islands'], ['MRT', 'Mauritania'], ['MUS', 'Mauritius'], ['MEX', 'Mexico'], ['FSM', 'Micronesia, Federated States of'], ['MDA', 'Moldova'], ['MCO', 'Monaco'], ['MNG', 'Mongolia'], ['MNE', 'Montenegro'], ['MAR', 'Morocco'], ['MOZ', 'Mozambique'], ['NAM', 'Namibia'], ['NPL', 'Nepal'], ['NLD', 'Netherlands'], ['NCL', 'New Caledonia'], ['NZL', 'New Zealand'], ['NIC', 'Nicaragua'], ['NGA', 'Nigeria'], ['NER', 'Niger'], ['NIU', 'Niue'], ['MNP', 'Northern Mariana Islands'], ['NOR', 'Norway'], ['OMN', 'Oman'], ['PAK', 'Pakistan'], ['PLW', 'Palau'], ['PAN', 'Panama'], ['PNG', 'Papua New Guinea'], ['PRY', 'Paraguay'], ['PER', 'Peru'], ['PHL', 'Philippines'], ['POL', 'Poland'], ['PRT', 'Portugal'], ['PRI', 'Puerto Rico'], ['QAT', 'Qatar'], ['ROU', 'Romania'], ['RUS', 'Russia'], ['RWA', 'Rwanda'], ['KNA', 'Saint Kitts and Nevis'], ['LCA', 'Saint Lucia'], ['MAF', 'Saint Martin'], ['SPM', 'Saint Pierre and Miquelon'], ['VCT', 'Saint Vincent and the Grenadines'], ['WSM', 'Samoa'], ['SMR', 'San Marino'], ['STP', 'Sao Tome and Principe'], ['SAU', 'Saudi Arabia'], ['SEN', 'Senegal'], ['SRB', 'Serbia'], ['SYC', 'Seychelles'], ['SLE', 'Sierra Leone'], ['SGP', 'Singapore'], ['SXM', 'Sint Maarten'], ['SVK', 'Slovakia'], ['SVN', 'Slovenia'], ['SLB', 'Solomon Islands'], ['SOM', 'Somalia'], ['ZAF', 'South Africa'], ['SSD', 'South Sudan'], ['ESP', 'Spain'], ['LKA', 'Sri Lanka'], ['SDN', 'Sudan'], ['SUR', 'Suriname'], ['SWZ', 'Swaziland'], ['SWE', 'Sweden'], ['CHE', 'Switzerland'], ['SYR', 'Syria'], ['TWN', 'Taiwan'], ['TJK', 'Tajikistan'], ['TZA', 'Tanzania'], ['THA', 'Thailand'], ['TLS', 'Timor-Leste'], ['TGO', 'Togo'], ['TON', 'Tonga'], ['TTO', 'Trinidad and Tobago'], ['TUN', 'Tunisia'], ['TUR', 'Turkey'], ['TKM', 'Turkmenistan'], ['TUV', 'Tuvalu'], ['UGA', 'Uganda'], ['UKR', 'Ukraine'], ['ARE', 'United Arab Emirates'], ['GBR', 'United Kingdom'], ['USA', 'United States'], ['URY', 'Uruguay'], ['UZB', 'Uzbekistan'], ['VUT', 'Vanuatu'], ['VEN', 'Venezuela'], ['VNM', 'Vietnam'], ['VGB', 'Virgin Islands'], ['WBG', 'West Bank'], ['YEM', 'Yemen'], ['ZMB', 'Zambia'], ['ZWE', 'Zimbabwe']]


with open('./output/queries/q1_4.csv', 'rb') as csvfile:
    country_count = list(csv.reader(csvfile))
# find the abbreviation for each country
for row in country_count[1:]:
    ori_ctryName = row[0]
    for mapRow in ABBR_FULLNAME:
        if (ori_ctryName in mapRow[1].upper()):
            row.append(mapRow[0])
# mannally add abbreviation for those don't have a match
for row in country_count[1:]:
    if (row[0] == 'SOUTH KOREA'):
        row.append('PRK')
    elif (row[0] == 'BURMA (MYANMAR)'):
        row.append('MMR')
    elif (row[0] == 'SERBIA AND MONTENEGRO'):
        row.append('SRB')
    elif (row[0] == 'ST LUCIA'):
        row.append('LCA')
# delete those countries without a specified abbreviation
# adjust those countries has more than one abbreviations
for row in country_count[1:]:
    if (len(row) != 3):
        country_count.remove(row)
# adjust the title
country_count[0][0]= 'countryName'
country_count[0].append('abbr')
#output to csv file
outputCsv('./output/viz/PERM_Peers/ctryAbbr_count_Plotly.csv', country_count)
# give out a non-India Version
del country_count[1]
outputCsv('./output/viz/PERM_Peers/ctryAbbr_count_Plotly_NoIndia.csv', country_count)
# give out a non-India-China Version
del country_count[1]
outputCsv('./output/viz/PERM_Peers/ctryAbbr_count_Plotly_NoIndiaChina.csv', country_count)
# give out a non-India-China-Canada Version
del country_count[1]
outputCsv('./output/viz/PERM_Peers/ctryAbbr_count_Plotly_NoIndiaChinaCanada.csv', country_count)

# with open('./output/viz/PERM_Peers/ctryAbbr_count.csv', 'rb') as csvfile:
#     abbr_count_list = list(csv.reader(csvfile))
# abbr_count_dict = {}
# for row in abbr_count_list[1:]:
#     abbr_count_dict[row[0]] = int(row[1])
#
#
# worldmap_chart = pygal.maps.world.World()
# worldmap_chart.title = 'Where are they from?'
# worldmap_chart.add('2016 Fiscal Year', abbr_count_dict)
# worldmap_chart.render_in_browser()
