SplitPrice()
GetCookieFunctionality_ShowNotification()
let AllInputFormSubmitProject = document.querySelectorAll('[InputFormSubmitProject]')
let BtnSubmitProject = document.getElementById('BtnSubmitProject')

function StateButtonSubmitProject() {
    BtnSubmitProject.classList.remove('Disabled')
    BtnSubmitProject.addEventListener('click', SubmitProject)
    for (let Inp of AllInputFormSubmitProject) {
        let State = Inp.getAttribute('Valid') || 'false'
        if (State == 'false') {
            BtnSubmitProject.classList.add('Disabled')
            BtnSubmitProject.removeEventListener('click', SubmitProject)
        }
    }
}


function CancelProject(ID) {
    SendAjax('/U/Profile/CancelProject', {'ID': ID}, 'POST', function (response) {
        let Status = response.Status
        if (Status == '200') {
            ShowNotificationMessage(`پروژه شما با موفقیت لغو شد`, 'Success')
            document.querySelector(`[ProjectID='${ID}']`).remove()
        } else if (Status == '204' || Status == '404') {
            ShowNotificationMessage(`خطا | لفطا دقایقی دیگر مجددا امتحان کنید`, 'Success')
        }
    })
}

function SubmitProject() {
    let TitleProject = document.querySelector('[InputTitleSubmitProject]')
    let Technologies = document.querySelector('[InputTechnologiesSubmitProject]')
    let DeadLine = document.querySelector('[InputNumberDeadLineSubmitProject]')
    let Budget = document.querySelector('[InputBudgetSubmitProject]')
    let Description = document.querySelector('[InputDescriptionSubmitProject]')
    let Data = {
        'TitleProject': TitleProject.value,
        'Technologies': Technologies.value,
        'DeadLine': DeadLine.value,
        'Budget': Budget.value,
        'Description': Description.value,
    }
    SendAjax('/U/Profile/SubmitProject', Data, 'POST', function (response) {
        let Statue = response.Status
        if (Statue == '200') {
            SetCookieFunctionality_ShowNotification(`پروژه شما با موفقیت ثبت شد و اکنون در حال بررسی است`, 'Success', 7000, 2)
            location.href = '/U/Profile?ProjectChecking'
        } else if (Statue == '204') {
            ShowNotificationMessage(`لطفا مقادیر فرم را به درستی وارد نمایید`, 'Error', 7000)
        } else if (Statue == '205') {
            ShowNotificationMessage(`برای ثبت پروژه ابتدا باید  اطلاعات حود را تکمیل کنید`, 'Error', 7000)
            ActiveContainerAndIcon('Info')
        }
    })
}


function SetPriceInP(Price) {
    let Element = document.querySelector('[PriceForSubmitProject]')
    Element.setAttribute('Number', Price)
    SplitPrice(Element, true)
    Element.innerHTML += ' تومان '
}


let AllBtnAside = document.querySelectorAll('.ItemAsideWithContainer')
for (let Btn of AllBtnAside) {
    Btn.addEventListener('click', function (e) {
        let Btn = e.currentTarget
        let ClickShow = Btn.getAttribute('ClickShowContainer')
        let Container = document.querySelector(`[ContainerItemMenu=${ClickShow}]`)
        ActiveContainer(Container)
        ActiveIconMenuAside(Btn)
    })
}

function ActiveContainerAndIcon(Text) {
    ActiveContainer(document.querySelector(`[ContainerItemMenu='${Text}']`))
    ActiveIconMenuAside(document.querySelector(`[ClickShowContainer='${Text}']`))
}

function ActiveContainer(Container_ID) {
    let AllContainer = document.querySelectorAll('.ContainerBaseContent')
    for (let Container of AllContainer) {
        Container.classList.remove('ContainerContentIsShow')
    }
    try {
        Container_ID.classList.add('ContainerContentIsShow')
    } catch (e) {
        document.getElementById(Container_ID).classList.add('ContainerContentIsShow')
    }
}

function ActiveIconMenuAside(Icon) {
    let AllItemAside = document.querySelectorAll('.ItemAside')
    for (let Item of AllItemAside) {
        Item.classList.remove('ItemAsideActive')
    }
    Icon.classList.add('ItemAsideActive')
}

let FuncSetActiveContainer = ActiveContainer
let AttrSearchContainer = 'ContainerItemMenu'
let ValAttrContainerDefault = 'ProjectChecking'
let UrlContainer = window.location.href
let ValueForItemMenu = UrlContainer.split('?')[1]
if (ValueForItemMenu != undefined && ValueForItemMenu != '' && ValueForItemMenu != ' ') {
    let ItemsInMenuForURL = document.querySelector(`[${AttrSearchContainer}=${ValueForItemMenu}]`)
    if (ValueForItemMenu == 'Home') {
        GoToUrl('/')
    }
    if (ItemsInMenuForURL != null) {
        FuncSetActiveContainer(ItemsInMenuForURL)
        let Icon = document.querySelector(`[ClickShowContainer=${ValueForItemMenu}]`)
        ActiveIconMenuAside(Icon)
    } else {
        ItemsInMenuForURL = document.querySelector(`[${AttrSearchContainer}=${ValAttrContainerDefault}]`)
        FuncSetActiveContainer(ItemsInMenuForURL)
        let Icon = document.querySelector(`[ClickShowContainer=${ValAttrContainerDefault}]`)
        ActiveIconMenuAside(Icon)
    }
} else {
    ItemsInMenuForURL = document.querySelector(`[${AttrSearchContainer}=${ValAttrContainerDefault}]`)
    FuncSetActiveContainer(ItemsInMenuForURL)
    let Icon = document.querySelector(`[ClickShowContainer=${ValAttrContainerDefault}]`)
    ActiveIconMenuAside(Icon)
}


let AllInputFormInfoUser = document.querySelectorAll('[InputFormInfo]')

function StateButtonSubmitInfo() {
    let BtnSubmitInfo = document.getElementById('ButtonSubmitInfoUser')
    BtnSubmitInfo.classList.remove('Disabled')
    BtnSubmitInfo.addEventListener('click', SubmitInfoUser)
    for (let i of AllInputFormInfoUser) {
        let State = i.getAttribute('Valid') || 'false'
        if (State == 'false') {
            BtnSubmitInfo.classList.add('Disabled')
            BtnSubmitInfo.removeEventListener('click', SubmitInfoUser)
        }
    }
}

function SubmitInfoUser() {
    let UserNameAndFamily = document.querySelector('[InputNameAndFamilyUser]')
    let PhoneNumber = document.querySelector('[InputPhoneNumberUser]')
    let Email = document.querySelector('[InputEmailUser]')
    let Address = document.querySelector('[InputAddressUser]')
    let Data = {
        'UserNameAndFamily': UserNameAndFamily.value,
        'PhoneNumber': PhoneNumber.value,
        'Email': Email.value,
        'Address': Address.value
    }
    SendAjax('/U/Profile/SubmitInfo', Data, 'POST', function (response) {
        let Status = response.Status
        if (Status == '200') {
            ShowNotificationMessage(`اطلاعات شما با موفقیت ثبت شدند`, 'Success', 7000)
        } else if (Status == '204') {
            ShowNotificationMessage(`لطفا فیلدهای فرم را به درستی وارد نمایید`, 'Error', 7000)
        }
    })
}

function ClickShowContainerMenu(ID) {
    ActiveContainer(document.getElementById(ID))
    setTimeout(function () {
        CloseMenuContainer(document.getElementById('ContainerMenuHamburger'))
    })
}

function SignOutAccountIconMenu() {
    setTimeout(function () {
        CloseMenuContainer(document.getElementById('ContainerMenuHamburger'))
    })
    SignOutAccount()
}

