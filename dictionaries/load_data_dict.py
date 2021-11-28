# dictionary_mapping format:
# {
#     <CsvYear> : {
#         <CsvColumnName>: (<SqlTableName>, <SqlTableField>),
#         ...
#     }
#     ...
# }
dictionary_column_mapping = {
    'hospitalCases': ('casos_em_hospitais', 'casos_em_hospitais'),
    'capacityPillarFour': ('capacidade_teste_profissionais', 'capacidade_teste_profissionais'),
    'capacityPillarOneTwo': ('capacidade_teste_populacao', 'capacidade_teste_populacao'),
    'capacityPillarThree': ('capacidade_teste_anticorpos', 'capacidade_teste_anticorpos'),
    'covidOccupiedMVBeds': ('leitos_com_respiradores_ocupados', 'leitos'),
    'newAdmissions': ('admissoes_em_hospitais', 'admissoes'),
    'plannedCapacityByPublishDate': ('capacidade_planejada', 'capacidade_planejada'),
    'newVirusTests': ('novos_testes', 'numero_de_testes'),
    'newPeopleVaccinatedFirstDoseByPublishDate': ('pessoas_vacinadas_dose_1', 'pessoas_vacinadas_dose_1'),
    'newPeopleVaccinatedSecondDoseByPublishDate': ('pessoas_vacinadas_dose_2', 'pessoas_vacinadas_dose_2')
}