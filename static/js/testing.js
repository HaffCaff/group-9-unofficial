// test variables
let test1_value = ''
let test2_value = 0
let test5_list = []

// event targets
let test1_input = document.querySelector('#test1-input')
let test2_button = document.querySelector('#test2-button')
let test3_button = document.querySelector('#test3-button')
let test5_input = document.querySelector('#test5-input')

// outputs
let test1_output = document.querySelector('#test1-output')
let test2_output = document.querySelector('#test2-output')
let test4_output = document.querySelector('#test4-output')
let test5_output = document.querySelector('#test5-output')

function test1() {
    test1_value = test1_input.value
    test1_output.textContent = test1_value
}

function test2() {
    test2_value += 1
    test2_output.textContent = test2_value
}

function test3() {
    test2_value = 0
    test2_output.textContent = test2_value
}

function test4() {
    var ele = document.getElementsByName('fav_language');

    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked)
            document.getElementById("result").innerHTML
                = "Favorite Language: " + ele[i].value;
    }
}

function test5() {
    test5_list.push(test5_input.value)
    document.getElementById("list-contents").innerHTML = test5_list
}