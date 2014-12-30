$(document).ready(function() {
    var ENG = [
        {display: "Chemical Engineering", value: "CHE"},
        {display: "Civil Engineering", value: "CE"},
        {display: "Computer Science", value: "CS"},
        {display: "Electrical Engineering", value: "EE"},
        {display: "Environmental Engineering", value: "ENV"},
        {display: "Management Science and Engineering", value: "MS&E"},
        {display: "Materials Science and Engineering", value: "MSE"},
        {display: "Mechanical Engineering", value: "ME"}];

    var HUA = [
        {display: "Art and Art History", value: "ART"},
        {display: "Classics", value: "CLASS"},
        {display: "English", value: "ENGL"},
        {display: "History", value: "HIST"},
        {display: "Linguistics", value: "LING"},
        {display: "Music", value: "MUS"},
        {display: "Philosophy", value: "PHL"},
        {display: "Languages", value: "LANG"}];

    var NAS = [
        {display: "Biology", value: "BIO"},
        {display: "Chemistry", value: "CHEM"},
        {display: "Communication", value: "COMM"},
        {display: "Economics", value: "ECON"},
        {display: "Mathematics", value: "MATH"},
        {display: "Physics", value: "PHY"},
        {display: "Political Science", value: "POLI"},
        {display: "Psychology", value: "PSYCH"},
        {display: "Statistics", value: "STAT"},
        {display: "Classics", value: "CLA"}];

    var EAS = [
        {display: "Earth Systems", value: "ESYS"},
        {display: "Energy Resources Engineering", value: "ERE"},
        {display: "Geological and Environmental Sciences", value: "GES"},
        {display: "Geophysics", value: "GP"}];

    $("#school").change(function () {
        var parent = $(this).val();

        switch (parent) {
            case 'Engineering':
                list(ENG);
                break;
            case 'Humanities and Arts':
                list(HUA);
                break;
            case 'Natural and Social Sciences':
                list(NAS);
                break;
            case 'Earth Sciences':
                list(EAS);
                break;
            default:
                break;
        }
    });


    function list(array_list) {
        $("#department").html("");
        $("#department").append("<option disabled selected></option>");
        $(array_list).each(function (i) {
            $("#department").append("<option value=\"" + array_list[i].value + "\">" + array_list[i].display + "</option>");
        });
    }
});