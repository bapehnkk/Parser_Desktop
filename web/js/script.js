// clear site input 
document.querySelector('.site-inp__cross').addEventListener('click', event => {
    document.querySelector('#site-inp').value = "";
});
// clear next site input 
document.querySelector('.site-inp__cross.next').addEventListener('click', event => {
    document.querySelector('#next-site-inp').value = "";
});


// add/remove "Chose selectors"
let i_li = 1;
document.querySelector('.selectors__add-btn').addEventListener('click', event => {
    document.querySelector('.selectors__ul').innerHTML +=
        "<li id=\"li-" + i_li + "\" class=\"selectors_li\">Chose selector<div class=\"div-input\"><input type=\"text\" class=\"main__inp\"><span onclick=\"del_li(" + i_li + ")\" class=\"cross selectors_li__cross\"></span></div></li>";
    i_li++;
});

function del_li(i) {
    document.querySelector('#li-' + i).remove();
}

// checkbox multipage-parsing

document.querySelector('.multipage-parsing input').addEventListener('change', event => {
    let b = document.querySelector('.multipage-parsing input').checked;
    console.log(b);
    if (document.querySelector('.multipage-parsing input').checked)
        document.querySelector('.multipage-parsing__true').style.display = "flex";
    else
        document.querySelector('.multipage-parsing__true').style.display = "none";
});


document.querySelector('.multipage-parsing__span').addEventListener('click', event => {
    if (document.querySelector('.multipage-parsing input').checked) {
        document.querySelector('.multipage-parsing input').checked = false;
        document.querySelector('.multipage-parsing__true').style.display = "none";
        document.querySelector('.multipage-parsing__span').classList.remove('active');
    } else {
        document.querySelector('.multipage-parsing input').checked = true;
        document.querySelector('.multipage-parsing__true').style.display = "flex";
        document.querySelector('.multipage-parsing__span').classList.add('active');
    }
});


document.querySelector('.download-btn').addEventListener('click', event => {
    document.querySelector('.download-btn a').click();
});

document.querySelector('.to-up').addEventListener('click', event => {
    window.scrollTo(pageXOffset, 0);
});