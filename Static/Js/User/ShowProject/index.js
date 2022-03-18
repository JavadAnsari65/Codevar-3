function ShowAndPayProject(ID, Type) {
    SendAjax('/U/Profile/GetProject', {'ID': ID}, 'POST', function (response) {
        let Status = response.Status
        let Object = response.Object
        if (Status == '200') {
            let Container = CreateContainerBlur('Default', 'ContainerProjectDetail')
            ClickOutSideContainer(Container, DeleteContainerBlur,'OutSide')
            let Node = `
                  <div class="Project ShowProject" ProjectID="${Object.id}">
        <div class="InfoProject">
            <div class="TitleProject">
                ${Object.Title}
            </div>
        </div>
        <div class="ContentProject">
            <div class="TimeSubmit">
                <div>
                    <p class="Label">ثبت شده در</p>
                    ${Object.TimePastSubmit}
                </div>
            </div>
            <div class="StateProject">
                <div>
                    <p class="Label">وضعیت</p>
                    <p class="ResultField">${Object.GetStateProject}</p>
                </div>
            </div>
            <div class="DeadLine DeadLineByUser">
                <div>
                    <p class="Label"> مهلت کاربر</p>
                    ${Object.DeadLineByUser}
                    روز
                    <i class="far fa-clock"></i>
                </div>
            </div>
            <div class="DeadLine DeadLineAdmin">
                <div>
                    <p class="Label">مهلت مورد نیاز مجموعه</p>
                        ${Object.DeadLineFinally}
                    روز
                    <i class="far fa-clock"></i>
                </div>
            </div>
            <div class="Budget BudgetAdmin">
                <p class="Label">قیمت نهایی</p>
                <p class="SplitNumber SplitPriceNumber"
                   Number="${Object.BudgetFinally}">${Object.BudgetFinally}</p>
                <p class="UnitPrice">تومان</p>
            </div>
            <div class="Budget BudgetUser ProjectContainer">
                <p class="Label">بودجه کاربر</p>
                <p class="SplitNumber SplitPriceNumber"
                   Number="${Object.BudgetByUser}">${Object.BudgetByUser}</p>
                <p class="UnitPrice">تومان</p>
            </div>
            <div class="Technologies ProjectContainer">
                <p class="Label">تکنولوژی ها</p>
                <p type="text">${Object.Technologies}</p>
            </div>
            <div class="Description DescriptionUser ProjectContainer">
                <p class="Label">توضیحات کاربر</p>
                <p class="TextDescriptionUser">
                    ${Object.Description}
                </p>
            </div>
            <div class="Description DescriptionAdmin ProjectContainer">
                <p class="Label">توضیحات مجموعه</p>
                <p class="TextDescriptionAdmin">
                    ${Object.DescriptionAdmin}
                </p>
            </div>
            <div class="ContainerContactUs">
                <p class="Label">راه های ارتباطی با ما</p>
                <div class="ItemsContactUs">
                    <i class="fab fa-telegram" Telegram></i>
                    <i class="fab fa-instagram" Instagram></i>
                    <i class="fa fa-envelope" Email></i>
                    <i class="fa fa-phone" Phone></i>
                </div>
            </div>
            ${Type == 'WaitPay' ? '<div class="ContainerBuyProject"><button class="BtnStyle_5" onclick="alert(\'انتقال به درگاه بانکی\')">پرداخت</button></div>' : ''}
        </div>
    </div>
          `
            Container.innerHTML = Node
            SplitPrice()
            ScrollOnElement(null, Container)
        } else if (Status == '204') {
            ShowNotificationMessage('خطا | لطفا دقایقی دیگر امتحان کنید', 'Error', 7000)
        }
    })
}