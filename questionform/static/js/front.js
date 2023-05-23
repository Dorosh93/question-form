$(document).ready(function() {
    const comp = document.getElementById('comp').value;
    set_companies();
    $('#id_form_company').val(comp);
    conpany_onchange();
});


function conpany_onchange() {
    const company = $('#id_form_company').val();
    document.getElementById('comp').innerHTML = company;
    if (company === 'другое'){ 
        $('#id_form_title').prop('required', true);
        $('#new_comp').prop('hidden', false);
    } else {
        $('#id_form_title').prop('required', false);
        $('#new_comp').prop('hidden', true);
    }
}

function set_companies() {
    const division = $('#id_form_division :selected').text();
    const division_to_companies = JSON.parse(document.getElementById('dict').value);
    if (division === '---------'){
        const list_comp = [];
    } else{
        let list_comp = division_to_companies[division];
        list_comp[list_comp.length] = 'другое'
    }
    $('#id_form_company').find('option').remove();
    for (let i = 0; i < list_comp.length; i++) {
        $('<option value="' + list_comp[i] + '">' + list_comp[i] + '</option>').appendTo('#id_form_company');
    }
    conpany_onchange();
}
