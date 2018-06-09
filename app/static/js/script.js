document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems);
    
    elems = document.querySelectorAll('.modal');
    instance = M.Modal.init(elems);
});
