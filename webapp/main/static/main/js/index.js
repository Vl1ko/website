document.querySelector('button').addEventListener('click', myClick)

function myClick(){
    let gl1 = document.querySelector('.i3-1').value;
    let gl2 = document.querySelector('.i3-2').value;
    let gl3_1 = document.querySelector('.i3-3-1').value;
    let gl3_2 = document.querySelector('.i3-3-2').value;
    let gl3_3 = document.querySelector('.i3-3-3').value;
    let gl3_4 = document.querySelector('.i3-3-4').value;
    let gl4_1 = document.querySelector('.i3-4-1').value;
    let gl4_2 = document.querySelector('.i3-4-2').value;
    let gl5_1 = document.querySelector('.i3-5-1').value;
    let gl5_2 = document.querySelector('.i3-5-2').value;
    let gl6 = document.querySelector('.i4-1').value;
    let gl7 = document.querySelector('.i4-2').value;
    let gl8 = document.querySelector('.i4-3').value;
    let gl9 = document.querySelector('.i4-4').value;
    document.querySelector('.p1').innerHTML = 'Глава 1';
    document.querySelector('.t1').innerHTML = gl1;
    document.querySelector('.p2').innerHTML = 'Глава 2';
    document.querySelector('.t2').innerHTML = gl2;
    document.querySelector('.p3').innerHTML = 'Глава 3';
    document.querySelector('.t3-1').innerHTML = gl3_1;
    document.querySelector('.t3-2').innerHTML = gl3_2;
    document.querySelector('.t3-3').innerHTML = gl3_3;
    document.querySelector('.t3-4').innerHTML = gl3_4;
    document.querySelector('.p4').innerHTML = 'Глава 4';
    document.querySelector('.t4-1').innerHTML = gl4_1;
    document.querySelector('.t4-2').innerHTML = gl4_2;
    document.querySelector('.t5-1').innerHTML = gl5_1;
    document.querySelector('.t5-2').innerHTML = gl5_2;
    // document.querySelector('.p6').innerHTML = 'Что делает эту историю уникальной?';
    document.querySelector('.t6-1').innerHTML = gl6;
    // document.querySelector('.p7').innerHTML = 'Есть ли у истории продолжение?';
    document.querySelector('.t6-2').innerHTML = gl7;
    // document.querySelector('.p8').innerHTML = 'Есть ли у героя последователи?';
    document.querySelector('.t6-3').innerHTML = gl8;
    // document.querySelector('.p9').innerHTML = 'Это был единичный случай?';
    document.querySelector('.t6-4').innerHTML = gl9;
}