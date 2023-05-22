$(document).ready(function() {
    var comp = document.getElementById('comp').value;
    console.log(comp)
    get_comp();
    $('#id_form_company').val(comp);
    new_comp();
});


function new_comp() {
    let val = $('#id_form_company').val();
    document.getElementById('comp').innerHTML = val;
    if (val === 'другое'){ 
        $('#id_form_title').prop('required', true);
        $('#new_comp').prop('hidden', false);
    } else {
        $('#id_form_title').prop('required', false);
        $('#new_comp').prop('hidden', true);
    }
}

function get_comp() {
    let val = $('#id_form_division :selected').text();
    var dict = document.getElementById('dict').value;
    var diction = JSON.parse(dict.replaceAll("'", '"'));
    if (val === '---------'){
        var list_comp = [];
    } else{
        var list_comp = diction[val];
        list_comp[list_comp.length] = 'другое'
    }
    $('#id_form_company').find('option').remove();
    for (var i = 0; i < list_comp.length; i++) {
        $('<option value="' + list_comp[i] + '">' + list_comp[i] + '</option>').appendTo('#id_form_company');
    }
    new_comp();
}
