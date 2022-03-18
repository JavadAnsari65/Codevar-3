SplitPrice()

function GetWorkSample(Element) {
    let ID = Element.getAttribute('ID_Sample')
    SendAjax('/M/Profile/WorkSample/Get', {'ID': ID}, 'POST', function (response) {
        let Status = response.Status
        if (Status == '200') {
            ShowWorkSample(response.Object)
        } else if (Status == '403') {
            ShowNotificationMessage(`شما دسترسی ندارید`, 'Error')
        }
    })
}

function ShowWorkSample(Object) {
    let Container = CreateContainerBlur()
    let NodeIconWithLike = `
                <i class="${Object.Liked == 'true' ? 'fa BtnLikeWorkSample ' : 'far'} fa-heart" onclick=LikeDisLikeWorkSample(this,'${Object.ID}') Liked="${Object.Liked}"></i>
            `
    let NodeIconNoWithLike = `
                <i class="${Object.Liked == 'true' ? 'fa BtnLikeWorkSample ' : 'far'} fa-heart" Liked="${Object.Liked}"></i>
            `
    let Node = `
                <i class="fa fa-times" onclick="document.body.click()"></i>
                <div class="ContainerShowWorkSample">
                    <div class="ContainerImageSample">
                        <img src="${Object.ImageUrl}" alt="${Object.Title}">
                    </div>
                    <div class="ContainerInfoSample">
                        <div class="ContainerItemInfoSample" TitleSample>
                            <p class="TitleLabelSample">موضوع :</p>
                            <p class="TitleSample">${Object.Title}</p>
                            <div class="float-left ContainerItemInfoSample" TimePast title="زمان انتشار">
                                <i class="far fa-clock"></i>
                                <p>${Object.TimePast}</p>
                            </div>
                            <br>
                            <div class="float-left ContainerItemInfoSample" Like title="پسندیدن">            
                                ${Object.StateRequest == 'User' ? NodeIconWithLike : NodeIconNoWithLike}
                                <p NumberLike>${Object.Likes}</p>
                            </div>
                        </div>

                        <div class="ContainerItemsInfoSample">
                            <div class="ContainerItemInfoSample">
                                <p class="TitleLabelSample">برنامه نویس :</p>
                                <p class="ResultLabelSample">${Object.UserNameCreator}</p>
                            </div>
                            <div class="ContainerItemInfoSample">
                                <p class="TitleLabelSample">آدرس :</p>
                                
                                <a clas="ResultLabelSample" href='${Object.Address}'target="_blank">مشاهده</a>
                            </div>
                            <div class="ContainerItemInfoSample">
                                <p class="TitleLabelSample">تکنولوژی ها :</p>
                                <p class="ResultLabelSample">${Object.Technologies}</p>
                            </div>
                            <div class="ContainerItemInfoSample">
                                <p class="TitleLabelSample">زمان صرف شده :</p>
                                <p class="ResultLabelSample">${Object.TimeElapsed} روز</p>
                            </div>
                        </div>
                        <div class="ContainerItemInfoSample" Description>
                            <p class="TitleLabelSample">توضیحات :</p>
                            <p class="ResultLabelSample">${Object.Description}</p>
                        </div>
                    </div>
                </div>
                      `
    Container.innerHTML = Node
    ClickOutSideContainer(Container, function () {
        DeleteContainerBlur()
    }, 'OutSide')
    ScrollOnElement(null, Container)
}


function LikeDisLikeWorkSample(Icon, ID) {
    let Element = Icon.parentNode
    let NumberLike = Element.querySelector('[NumberLike]')
    let State = Icon.getAttribute('Liked') || 'false'
    if (State == 'false') {
        Icon.classList.remove('far')
        Icon.classList.add('fa')
        Icon.setAttribute('Liked', 'true')
        NumberLike.innerHTML = parseInt(NumberLike.innerText) + 1
    } else {
        Icon.classList.add('far')
        Icon.classList.remove('fa')
        Icon.setAttribute('Liked', 'false')
        NumberLike.innerHTML = parseInt(NumberLike.innerText) - 1
    }
    SendAjax('/M/WorkSample/LikeDisLike', {'State': State, 'ID': ID}, 'POST', function (response) {
        if (response.Status != '200') {
            ShowNotificationMessage(`مشکلی پیش امده است`, 'Error')
        }
    })
}