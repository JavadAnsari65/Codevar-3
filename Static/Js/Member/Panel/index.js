GetCookieFunctionality_ShowNotification()
SplitPrice()
let ButtonAddWorkSample = document.getElementById('ButtonAddWorkSample')
ButtonAddWorkSample.onclick = function () {
    let Container = CreateContainerBlur('Default', 'ContainerAddWorkSampleBlur')
    let Node = `
                    <div class="TitleContainer">
                        <p>نمونه کار</p>
                    </div>
                     <form action="/M/Profile/WorkSample/Add" method="POST" enctype="multipart/form-data" id="ContainerFormWorkSample">
                            <div class="ContainerItemForm">
                                <p class="LabelInput">موضوع</p>
                                <div class="ContainerInputIcon">
                                    <input type="text" name="Title" maxlength="100" oninput="CheckInputValidations(this,'1','100');StateButtonAddWorkSample()" InputFormWorkSample Valid="false">
                                </div>
                            </div>
                            <div class="ContainerItemForm">
                                <p class="LabelInput">آدرس نمونه کار</p>
                                <div class="ContainerInputIcon">
                                    <input type="text" dir="ltr" name="AddressWorkSample" maxlength="150" oninput="CheckInputValidations(this,'1','150');StateButtonAddWorkSample()" InputFormWorkSample Valid="false">
                                </div>
                            </div>
                            <div class="ContainerItemForm">
                                <p class="LabelInput">مقدار زمان سپری شده (روز)</p>
                                <div class="ContainerInputIcon">
                                    <input type="number" name="TimeElapsed" maxlength="20" oninput="CheckInputValidations(this,'0','20','Input','Number');StateButtonAddWorkSample()" InputFormWorkSample Valid="false">
                                </div>
                            </div>
                            <div class="ContainerItemForm">
                                <p class="LabelInput">تکنولوژی های استفاده شده</p>
                                <div class="ContainerInputIcon">
                                    <input type="text" dir="ltr" name="Technologies" maxlength="300" oninput="CheckInputValidations(this,'1','300');StateButtonAddWorkSample()" InputFormWorkSample Valid="false">
                                </div>
                            </div>
                            <div class="ContainerItemForm">
                                <p class="LabelInput">توضیحات</p>
                                <div class="ContainerInputIcon">
                                    <textarea  rows="5" name="Description" maxlength="1000" oninput="CheckInputValidations(this,'1','1000');StateButtonAddWorkSample()" InputFormWorkSample Valid="false"></textarea>
                                </div>
                            </div>
                            <div class="ContainerItemForm">
                                <p class="LabelInput">عکس</p>
                                <div class="ContainerInputIcon">
                                    <input type="file" name="Image" Valid="false" oninput="ValidationFile(this);StateButtonAddWorkSample()" InputFormWorkSample State="MostGet">
                                </div>
                            </div>
                            <div class="ContainerButtonAddWorkSample">
                                <button BtnCancelWorkSample onclick="document.body.click()" type="button">لغو</button>
                                <button BtnAddWorkSample class="BtnAddWorkSample" type="button">افزودن</button>
                            </div>
                     </form>
                `
    Container.innerHTML = Node
    ClickOutSideContainer(Container, function () {
        DeleteContainerBlur()
    })
}


let ButtonAddSkill = document.getElementById('ButtonAddSkill')
ButtonAddSkill.onclick = function () {
    CreateSkill()
}
let ContainerSkills = document.getElementById('ContainerSkills')

function StateButtonAddWorkSample() {
    let AllInputFormWorkSample = document.querySelectorAll('[InputFormWorkSample]')
    let ButtonAddWorkSample = document.querySelector('[BtnAddWorkSample]')
    ButtonAddWorkSample.classList.add('BtnStyleActive1')
    ButtonAddWorkSample.type = 'submit'
    for (let i of AllInputFormWorkSample) {
        let State = i.getAttribute('Valid') || 'false'
        if (State == 'false') {
            ButtonAddWorkSample.type = 'button'
            ButtonAddWorkSample.classList.remove('BtnStyleActive1')
        }
    }
}


function EditSample(Element) {
    let ID = Element.getAttribute('ID_Sample')
    SendAjax('/M/Profile/WorkSample/Get', {'ID': ID}, 'POST', function (response) {
        (function () {
            let Container = CreateContainerBlur('Default', 'ContainerEditWorkSampleBlur')
            ClickOutSideContainer(Container, function () {
                DeleteContainerBlur()
            }, 'OutSide')
            if (response.Status == '200') {
                let Object = response.Object
                let Node = `
                             <div class="TitleContainer">
                                <p> تغییر نمونه کار</p>
                             </div>
                     <form action="/M/Profile/WorkSample/Edit" method="POST" enctype="multipart/form-data" id="ContainerFormWorkSample">
                            <input type="hidden" name="ID_Sample" value="${Object.ID}">
                            <div class="ContainerItemForm">
                                <p class="LabelInput">موضوع</p>
                                <div class="ContainerInputIcon">
                                    <input type="text" name="Title" class="InputValid" value="${Object.Title}" maxlength="100" oninput="CheckInputValidations(this,'1','100');StateButtonEditWorkSample()" InputEditFormWorkSample Valid="true">
                                </div>
                            </div>
                            <div class="ContainerItemForm">
                                <p class="LabelInput">آدرس نمونه کار</p>
                                <div class="ContainerInputIcon">
                                    <input type="text" name="AddressWorkSample" class="InputValid" value="${Object.Address}" maxlength="150" oninput="CheckInputValidations(this,'1','150');StateButtonEditWorkSample()" InputEditFormWorkSample Valid="true">
                                </div>
                            </div>
                            <div class="ContainerItemForm">
                                <p class="LabelInput">مقدار زمان سپری شده (روز)</p>
                                <div class="ContainerInputIcon">
                                    <input type="number" name="TimeElapsed" class="InputValid" value="${Object.TimeElapsed}" maxlength="20" oninput="CheckInputValidations(this,'0','20','Input','Number');StateButtonEditWorkSample()" InputEditFormWorkSample Valid="true">
                                </div>
                            </div>
                            <div class="ContainerItemForm">
                                <p class="LabelInput">تکنولوژی های استفاده شده</p>
                                <div class="ContainerInputIcon">
                                    <input type="text" dir="ltr" name="Technologies" class="InputValid" value="${Object.Technologies}" maxlength="300" oninput="CheckInputValidations(this,'1','300');StateButtonEditWorkSample()" InputEditFormWorkSample Valid="true">
                                </div>
                            </div>
                            <div class="ContainerItemForm">
                                <p class="LabelInput">توضیحات</p>
                                <div class="ContainerInputIcon">
                                    <textarea  rows="5" name="Description"  maxlength="1000" class="InputValid" oninput="CheckInputValidations(this,'1','1000');StateButtonEditWorkSample()" InputEditFormWorkSample Valid="true">${Object.Description}</textarea>
                                </div>
                            </div>
                            <div class="ContainerItemForm">
                                <p class="LabelInput">عکس</p>
                                <div class="ContainerInputIcon">
                                    <div class="ButtonIconDelete" BtnDeleteImageFormEditWorkSample onclick="RemoveImageFormEditWorkSample(this,this.parentNode)" >
                                    حذف
                                        <i class="fa fa-trash"></i>
                                    </div>
                                    <input type="hidden" InputStateImageFormEditWorkSample name="StateGetImage" value="Geted">
                                    <input type="file" name="Image" Valid="true" InputImageFormEditWorkSample class="InputValid" oninput="ValidationFile(this);StateButtonEditWorkSample()" InputEditFormWorkSample State="Geted">
                                    <a href="${Object.ImageUrl}" LinkUrlImageFormEditWorkSample >${Object.ImageUrl}</a>

                                </div>
                            </div>
                            <div class="ContainerButtonAddWorkSample">
                                <button BtnCancelWorkSample onclick="document.body.click()" type="button">لغو</button>
                                <button BtnEditWorkSample class="BtnEditWorkSample" type="button">ثبت</button>
                            </div>
                         </form>
                        `
                Container.innerHTML = Node
            }
        })()
    })
}

function StateButtonEditWorkSample() {
    let Button = document.querySelector('[BtnEditWorkSample]')
    let AllInputsEditWorkSample = document.querySelectorAll('[InputEditFormWorkSample]')

    Button.classList.add('BtnStyleActive1')
    Button.type = 'submit'

    for (let i of AllInputsEditWorkSample) {
        let State = i.getAttribute('Valid') || 'false'
        if (State == 'false') {
            Button.classList.remove('BtnStyleActive1')
            Button.type = 'button'
        }
    }
}

function RemoveImageFormEditWorkSample(Btn, Element) {
    Btn.classList.add('d-none')
    let Link = Element.querySelector('[LinkUrlImageFormEditWorkSample]')
    let Input = Element.querySelector('[InputImageFormEditWorkSample]')
    let StateInputImage = Element.querySelector('[InputStateImageFormEditWorkSample]')
    Link.classList.add('d-none')
    Input.classList.remove('InputValid')
    Input.setAttribute('Valid', 'false')
    Input.setAttribute('State', 'MostGet')
    StateInputImage.setAttribute('value', 'MostGet')
    StateButtonEditWorkSample()

}

function RemoveSample(Element) {
    CreateMessage_Alert(`ایا از پاک کردن نمونه کار خود مطمعن هستید ؟`, function () {
        let ID = Element.getAttribute('ID_Sample')
        SendAjax('/M/Profile/WorkSample/Remove', {'ID': ID}, 'POST', function (response) {
            let Status = response.Status
            if (Status == '200') {
                Element.remove()
                ShowNotificationMessage('نمونه کار شما با موفقیت حذف شد', 'Success')
            } else{
                ShowNotificationMessage(response.Status_Text, 'Error')
            }
        })
    })
}


function CreateSkill() {
    let ContainerBlur = CreateContainerBlur('Default', 'ContainerAddSkillBlur')
    let Node = `
                    <div class="TitleContainer">
                        <p>مهارت</p>
                    </div>
                     <div class="ContainerFormSkill">
                        <div class="ContainerRightFormSkill">
                                            <div class="ContainerItemForm">
                                                <p class="LabelInput">
                                                    عنوان مهارت
                                                </p>
                                                <div class="ContainerInputIcon">
                                                    <input type="text" oninput="CheckInputValidations(this,'1','100');StateButtonAddSkill(this)" maxlength="100" valid="false" InputTitleSkill>
                                                </div>
                                            </div>
                                            <div class="ContainerItemForm">
                                                <p class="LabelInput">
                                                    مقدار مهارت شما
                                                </p>
                                                <div ValueSkillInput>
                                                    <input type="range" max="100" value="50" InputRangeSkill oninput="ChangeValueInputRangeSkill(this)">
                                                    <p class="ValueRangeSkill" ValueOfSkill>50%</p>
                                                </div>
                                            </div>
                        </div>
                        <div class="ContainerLeftFormSkill">
                        <div class="ContainerItemForm">
                                                <p class="LabelInput">
                                                    توضیحات (دلخواه)
                                                </p>
                                                <div class="ContainerInputIcon">
                                                  <textarea  rows="3" maxlength="1000" InputDescriptionSkill></textarea>
                                                </div>
                                            </div>
                        </div>
                    </div>

                    <div class="ContainerButtonAddSkill">
                        <button BtnCancelSkill onclick="document.body.click()">لغو</button>
                        <button BtnAddSkill>افزودن</button>
                    </div>
                `
    ClickOutSideContainer(ContainerBlur, function () {
        DeleteContainerBlur()
    })
    ContainerBlur.innerHTML = Node
}

function StateButtonAddSkill(InputTitleSkill) {
    let Valid = InputTitleSkill.getAttribute('Valid') || 'false'
    let BtnAddSkill = document.querySelector('[BtnAddSkill]')
    if (Valid == 'true') {
        BtnAddSkill.classList.add('BtnAddSkillActive')
        BtnAddSkill.setAttribute('onclick', 'AddSkill()')
    } else {
        BtnAddSkill.classList.remove('BtnAddSkillActive')
        BtnAddSkill.removeAttribute('onclick')
    }
}

function AddSkill() {
    let InputTitleSkill = document.querySelector('[InputTitleSkill]')
    let InputRangeSkill = document.querySelector('[InputRangeSkill]')
    let InputDescriptionSkill = document.querySelector('[InputDescriptionSkill]')
    let Data = {
        'TitleSkill': InputTitleSkill.value,
        'ValueSkill': InputRangeSkill.value,
        'DescriptionSkill': InputDescriptionSkill.value
    }
    SendAjax('Profile/Skill/Add', Data, 'POST', function (response) {
        if (response.Status == '200') {
            location.href = '/M/Profile?Skills'
            //AddSkillToContainerSkills(response.IDSkill, InputTitleSkill.value, InputRangeSkill.value, InputDescriptionSkill.value)
        } else {
            ShowNotificationMessage(`شما دسترسی ندارید`, 'Error')
        }
        document.body.click()
    })
}

function AddSkillToContainerSkills(ID, Title, Value, Description) {
    let ClassValueProgress = ''
    let ContainerSkills = document.getElementById('ContainerSkills')
    if (Value >= 75) {
        ClassValueProgress = 'ProgressSkillGood'
    } else if (Value <= 74 && Value >= 55) {
        ClassValueProgress = 'ProgressSkillAverage'
    } else if ((Value <= 54 && Value >= 35)) {
        ClassValueProgress = 'ProgressSkillLow'
    } else {
        ClassValueProgress = 'ProgressSkillVeryLow'
    }
    let Node = `
                         <div class="Skill" Skill>
                            <div class="ContainerEditDeleteSkill">
                                <i class="fa fa-trash" onclick="RemoveSkill(${ID},this.parentNode.parentNode)"></i>
                            </div>
                            <div class="TitleSkill">
                                <p TitleSkill>${Title}</p>
                            </div>
                            <div class="ContainerProgress ">
                                <progress class="ProgressSkill ${ClassValueProgress}" max="100" value="${Value}"></progress>
                                <p class="ValueRangeSkill">${Value}%</p>
                            </div>
                            <div class="ContainerDescriptionSkill">
                                <p>${Description}</p>
                            </div>
                        </div>
                `
    ContainerSkills.insertAdjacentHTML('beforeend', Node)
}


function ChangeValueInputRangeSkill(Input) {
    let ElementValueOfSkill = document.querySelector('[ValueOfSkill]')
    let Value = Input.value
    ElementValueOfSkill.innerHTML = Value + '%'
    ElementValueOfSkill.setAttribute('Color', 'Yellow')
    if (Value > 70) {
        ElementValueOfSkill.setAttribute('Color', 'Green')
    } else if (Value < 71 && Value > 50) {
        ElementValueOfSkill.setAttribute('Color', 'Blue')
    } else if (Value < 51 && Value > 30) {
        ElementValueOfSkill.setAttribute('Color', 'Yellow')
    } else if (Value < 31 && Value > 15) {
        ElementValueOfSkill.setAttribute('Color', 'Orange')
    } else if (Value < 16) {
        ElementValueOfSkill.setAttribute('Color', 'Red')
    }
}

function RemoveSkill(ID, Element) {
    CreateMessage_Alert(`ایا از حذف مهارت خود اطمینان دارید ؟`, function () {
        SendAjax('Profile/Skill/Remove', {'ID': ID}, 'POST', function (response) {
            let Status = response.Status
            if (Status == '200') {
                Element.remove()
                ShowNotificationMessage(`مهارت مورد نظر با موفقیت حذف شد`, 'Success')
            } else{
                ShowNotificationMessage(response.Status_Text,'Error')
            }
        })
    })
}

function EditSkill(Element) {
    let TitleSkill = Element.querySelector('[TitleSkill]')
    let InputTitle = Element.querySelector('[InputEditTitleSkill]')
    let ProgressSkill = Element.querySelector('[ProgressSkill]')
    let BtnEditSkill = Element.querySelector('[BtnEditSkill]')
    BtnEditSkill.classList.toggle('BtnActiveIconNeo')
    ProgressSkill.classList.add('d-none')
    InputTitle.value = TitleSkill.innerText
    TitleSkill.classList.add('d-none')

}


let InputFileImageInFormInfo = document.getElementById('InputImageFormInfo')
let ImageFormInfo = document.getElementById('ImageFormInfo')
let FormInfo = document.getElementById('ContainerFormInfo')

InputFileImageInFormInfo.onchange = function (e) {
    const [File] = InputFileImageInFormInfo.files
    if (File) {
        ImageFormInfo.src = URL.createObjectURL(File)
    }
}

let ButtonSubmitFormInfo = document.getElementById('ButtonSubmitFormInfo')
let AllInputFormInfo = document.querySelectorAll('[InputFormInformation]')

function SetStateButtonSubmitFormInfo() {
    ButtonSubmitFormInfo.classList.add('ButtonSubmitActive')
    ButtonSubmitFormInfo.setAttribute('type', 'submit')
    for (let i of AllInputFormInfo) {
        let StateValid = i.getAttribute('Valid') || 'false'
        if (StateValid == 'false') {
            ButtonSubmitFormInfo.classList.remove('ButtonSubmitActive')
            ButtonSubmitFormInfo.setAttribute('type', 'button')
        }
    }
}

SetStateButtonSubmitFormInfo()


function SetStateInputFile(Input) {
    let Element = Input.parentNode
    let LinkImage = Element.querySelector('a')
    LinkImage.innerText = ''
    document.getElementById('ImageStateFormInfo').setAttribute('value', 'MostGet')
}


//--------------------- Show Item Menu  -----------------

let AllItemsMenu = document.querySelectorAll('[ItemMenu]')
let AllItemsMenuContainer = document.querySelectorAll('[ContainerItemMenu]')
let ContainerMain = document.getElementById('ContainerMain')
for (let i of AllItemsMenu) {
    i.onclick = function (e) {
        let Element = e.currentTarget
        ActiveContainer(Element)
    }
}


function ActiveContainer(Element) {
    CloseAllItemsMenu()
    Element.querySelector('i').classList.replace('fal', 'fa')
    Element.classList.add('ItemAsideMenuActive')
    let ContainerItemMenu = document.querySelector(`[ContainerItemMenu=${Element.getAttribute('ItemMenu')}]`)
    ContainerItemMenu.classList.add('AnimationTopToBottom')
    ContainerItemMenu.classList.add('ContainerItemMenuIsActive')
}

function CloseAllItemsMenu() {
    ContainerMain.classList.remove('AnimationTopToBottom')
    for (let i of AllItemsMenu) {
        i.classList.remove('ItemAsideMenuActive')
        i.querySelector('i').classList.replace('fa', 'fal')
    }
    for (let i of AllItemsMenuContainer) {
        i.classList.remove('ContainerItemMenuIsActive')
        i.classList.remove('AnimationTopToBottom')
    }
}

let FuncSetActiveContainer = ActiveContainer
let AttrSearchContainer = 'ItemMenu'
let ValAttrContainerDefault = 'Profile'
let UrlContainer = window.location.href
let ValueForItemMenu = UrlContainer.split('?')[1]
if (ValueForItemMenu != undefined && ValueForItemMenu != '' && ValueForItemMenu != ' ') {
    let ItemsInMenuForURL = document.querySelector(`[${AttrSearchContainer}=${ValueForItemMenu}]`)
    if (ValueForItemMenu == 'Home') {
        GoToUrl('/')
    }
    if (ItemsInMenuForURL != null) {
        FuncSetActiveContainer(ItemsInMenuForURL)
    }
} else {
    ItemsInMenuForURL = document.querySelector(`[${AttrSearchContainer}=${ValAttrContainerDefault}]`)
    FuncSetActiveContainer(ItemsInMenuForURL)
}