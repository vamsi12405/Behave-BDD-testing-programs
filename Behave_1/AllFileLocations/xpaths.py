xpath1={
    "//input[@placeholder='First Name']'":"vamsi",
    "//input[@placeholder='Last Name']":"krishna",
    "//textarea[@ng-model='Adress']":"Bangalore",
    "//input[@type='email']":"vamsi23@gmail.com",
    "//input[@type='tel']":"9874569823"
}

xpath2={"Male":"//input[@value='Male']",
        "Female":"//input[@value='FeMale']"
        }

xpath3={"Cricket":"//input[@id='checkbox1']",
        "Movies":"//input[@id='checkbox2']",
        "Hockey":"//input[@id='checkbox3']"}

xpath4={
    "Languages":"//ul//li[@class='ng-scope']//a[contains(text(),'English')]",
    "Select":"//select[@id='Skills']",
    "Country":"//span[@title='Denmark']"
}
xpath5={
    "Year":"//select[@placeholder='Year']",
    "Month":"//select[@placeholder='Month']",
    "Day":"//select[@placeholder='Day']"
}

xpath6={"Password_1":"(//input[@type='password'])[1]",
        "Confirm_Password_1":"(//input[@type='password'])[2]"}

xpath7={
    "Button":"//button[@type='submit']"
    }

list=[xpath2,xpath3,xpath4,xpath5,xpath6,xpath7]