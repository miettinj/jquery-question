from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from . import forms as fm
from django.forms import formset_factory

#def formset(request, formset_class, template):
def formset(request, template):
    a_vars_init = [{'technical_name': 'Lkm', 'decimals': '0', 'decimals_format': '0', 'units': 'lukumaara', 'domain': None, 'px_map': None, 'var_type': None, 'var_direction': 'col', 'var_name_fi': 'Asuntokuntien lukumaara', 'var_name_sv': 'Antal bostadshusholl', 'var_name_en': 'Number of household-dwelling units', 'var_desc_fi': '', 'var_desc_sv': '', 'var_desc_en': '', 'var_class_id': None}, {'technical_name': 'asuntovaestoa', 'decimals': '0', 'decimals_format': '0', 'units': 'lukumaara', 'domain': None, 'px_map': None, 'var_type': None, 'var_direction': 'col', 'var_name_fi': 'Asuntovaeston lukumaara', 'var_name_sv': 'Antal personer i bostadshushollet', 'var_name_en': 'Number of dwelling population', 'var_desc_fi': '', 'var_desc_sv': '', 'var_desc_en': '', 'var_class_id': None}]
    l_vars_init = [{'technical_name': 'alue', 'classification': 'alue_23_20220101', 'elimination': 'SSS', 'domain': '_kunta_2021', 'px_map': '', 'scaletype': 'nominal', 'prependcode': '', 'var_type': 'Classificatory', 'var_direction': 'row', 'var_name_fi': 'Alue', 'var_name_sv': 'Omrode', 'var_name_en': 'Area', 'var_desc_fi': '', 'var_desc_sv': '', 'var_desc_en': '', 'var_class_id': 'alue_23_20220101'}, {'technical_name': 'akoko_v4', 'classification': 'asuntokuntakoko_3_20190102', 'elimination': 'SSS', 'domain': '', 'px_map': '', 'scaletype': 'nominal', 'prependcode': '', 'var_type': 'Classificatory', 'var_direction': 'row', 'var_name_fi': 'Asuntokunnan koko', 'var_name_sv': 'Bostadshushollets storlek', 'var_name_en': 'Size of household-dwelling unit', 'var_desc_fi': '', 'var_desc_sv': '', 'var_desc_en': '', 'var_class_id': 'asuntokuntakoko_3_20190102'}, {'technical_name': 'hape', 'classification': 'hallintaperuste_5_20120101', 'elimination': 's', 'domain': '', 'px_map': '', 'scaletype': 'nominal', 'prependcode': '', 'var_type': 'Classificatory', 'var_direction': 'row', 'var_name_fi': 'Hallintaperuste', 'var_name_sv': 'Upplotelseform', 'var_name_en': 'Tenure status', 'var_desc_fi': '', 'var_desc_sv': '', 'var_desc_en': '', 'var_class_id': 'hallintaperuste_5_20120101'}, {'technical_name': 'taty', 'classification': 'talotyyppi_4_20210101', 'elimination': 'S', 'domain': '', 'px_map': '', 'scaletype': 'nominal', 'prependcode': '', 'var_type': 'Classificatory', 'var_direction': 'row', 'var_name_fi': 'Talotyyppi', 'var_name_sv': 'Hustyp', 'var_name_en': 'Type of building', 'var_desc_fi': '', 'var_desc_sv': '', 'var_desc_en': '', 'var_class_id': 'talotyyppi_4_20210101'}, {'technical_name': 'timeperiod', 'classification': '', 'elimination': '', 'domain': '', 'px_map': '', 'scaletype': '', 'prependcode': '', 'var_type': 'Time', 'var_direction': 'row', 'var_name_fi': 'Ajankohta', 'var_name_sv': '', 'var_name_en': '', 'var_desc_fi': '', 'var_desc_sv': '', 'var_desc_en': '', 'var_class_id': ''}]

    SingleClsVariableFormSet = formset_factory(fm.SingleClsVariable)
    singeclsvar_fs = SingleClsVariableFormSet(prefix='fs_luok')

    SingleNumVariableFormSet = formset_factory(fm.SingleNumVariable)
    singenumvar_fs = SingleNumVariableFormSet(prefix='fs_num')

    singeclsvar_fs = SingleClsVariableFormSet(
        prefix='fs_luok', initial=l_vars_init)
    singenumvar_fs = SingleNumVariableFormSet(
        prefix='fs_num', initial=a_vars_init)

    return render_to_response(template,{'singelclsvars_fs': singeclsvar_fs, 'singelnumvars_fs': singenumvar_fs, },
        context_instance=RequestContext(request))

