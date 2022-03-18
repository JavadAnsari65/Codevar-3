let AllBtnLikeMember = document.querySelectorAll('[BtnLikeMember]')
for (let Btn of AllBtnLikeMember) {
    Btn.onclick = function (e) {
        let Icon = e.currentTarget
        let ID = Icon.getAttribute('IDMember')
        let ElementNumberLike = Icon.parentNode.querySelector('[NumberLikeMember]')
        let NumberLike = parseInt(ElementNumberLike.getAttribute('Number'))
        let Element = Icon.parentNode
        let Liked = Element.getAttribute('Liked') || 'false'
        if (Liked == 'false') {
            ElementNumberLike.innerHTML = NumberLike += 1
            Element.setAttribute('Liked', 'true')
            Icon.classList.replace('far', 'fa')
        } else {
            ElementNumberLike.innerHTML = NumberLike -= 1
            Element.setAttribute('Liked', 'false')
            Icon.classList.replace('fa', 'far')
        }
        LikeDisLikeMember(ID)
        ElementNumberLike.setAttribute('Number', NumberLike)
        SplitPrice(ElementNumberLike)
    }
}

function LikeDisLikeMember(ID) {
    SendAjax('/M/LikeDisLikeMember', {'ID': ID})
}