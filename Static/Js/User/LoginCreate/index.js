
        let ContainerLogin = document.getElementById('ContainerLogin')
        let ContainerCreate = document.getElementById('ContainerCreate')

        function ShowContainerCreate() {
            ContainerLogin.classList.add('ContainerIsHide')
            ContainerCreate.classList.remove('ContainerIsHide')
        }

        function ShowContainerLogin() {
            ContainerCreate.classList.add('ContainerIsHide')
            ContainerLogin.classList.remove('ContainerIsHide')
        }


        //                          Login
        let AllInputsLogin = document.querySelectorAll('[InputLogin]')

        function StateButtonLogin() {
            let ButtonLogin = document.getElementById('ButtonLogin')
            ButtonLogin.classList.add('ContainerButtonFormButtonActive')
            ButtonLogin.setAttribute('onclick', 'SubmitLogin()')
            for (let i of AllInputsLogin) {
                let State = i.getAttribute('Valid') || 'false'
                if (State == 'false') {
                    ButtonLogin.classList.remove('ContainerButtonFormButtonActive')
                    ButtonLogin.removeAttribute('onclick')
                }
            }
        }

        function SubmitLogin() {
            let UserName = document.querySelector('[InputUserNameLogin]').value
            let Password = document.querySelector('[InputPasswordLogin]').value
            let MessageLoginForm = document.getElementById('ContainerMessageLogin')
            let Data = {'UserName': UserName, 'Password': Password}

            SendAjax('/U/Login/LoginCheck', Data, 'POST', function (response) {
                let Status = response.Status
                if (Status == '200') {
                    let RememberMe = document.getElementById('InputRememberMELogin')
                    MessageLoginForm.querySelector('p').innerText = 'خوش امدید'
                    MessageLoginForm.classList.add('ContainerMessageSuccess')
                    MessageLoginForm.classList.remove('ContainerMessageError')
                    if (RememberMe.checked) {
                        SetCookie('QlYSqVS', response.QlYSqVS, 90)
                        SetCookie('YPtIeRC', response.YPtIeRC, 90)
                    } else {
                        SetCookie('QlYSqVS', response.QlYSqVS, 'Session')
                        SetCookie('YPtIeRC', response.YPtIeRC, 'Session')
                    }
                    location.href = '/U/Profile?Info'
                } else if (Status == '404') {
                    MessageLoginForm.querySelector('p').innerText = 'کاربری با این مشخصات یافت نشد'
                    MessageLoginForm.classList.add('ContainerMessageError')
                    MessageLoginForm.classList.remove('ContainerMessageSuccess')
                } else if (Status == '204') {
                    MessageLoginForm.querySelector('p').innerText = 'لطفا فیلد هارا به درستی پر نمایید'
                    MessageLoginForm.classList.add('ContainerMessageError')
                    MessageLoginForm.classList.remove('ContainerMessageSuccess')
                }
            })
        }

        //                      Create
        let AllInputsCreate = document.querySelectorAll('[InputCreate]')

        function StateButtonCreate() {
            let ButtonCreate = document.getElementById('ButtonCreate')
            ButtonCreate.classList.add('ContainerButtonFormButtonActive')
            ButtonCreate.setAttribute('onclick', 'SubmitCreate()')
            for (let i of AllInputsCreate) {
                let State = i.getAttribute('Valid') || 'false'
                if (State == 'false') {
                    ButtonCreate.classList.remove('ContainerButtonFormButtonActive')
                    ButtonCreate.removeAttribute('onclick')
                }
            }
        }

        let MessageCreateForm = document.getElementById('ContainerMessageCreate')

        function SubmitCreate() {
            let UserName = document.querySelector('[InputUserNameCreate]').value
            let Email = document.querySelector('[InputEmailCreate]').value
            let Password = document.querySelector('[InputPasswordCreate]').value
            let RememberMe = document.getElementById('InputRememberMECreate')
            let Data = {
                'UserName': UserName,
                'Email': Email,
                'Password': Password
            }
            SendAjax('/U/CreateAccount', Data, 'POST', function (response) {
                let Status = response.Status
                if (Status == '200') {
                    MessageCreateForm.querySelector('p').innerText = 'حساب شما با موفقیت ایجاد شد'
                    MessageCreateForm.classList.add('ContainerMessageSuccess')
                    MessageCreateForm.classList.remove('ContainerMessageError')
                    if (RememberMe.checked) {
                        SetCookie('QlYSqVS', response.QlYSqVS, 90)
                        SetCookie('YPtIeRC', response.YPtIeRC, 90)
                    } else {
                        SetCookie('QlYSqVS', response.QlYSqVS, 'Session')
                        SetCookie('YPtIeRC', response.YPtIeRC, 'Session')
                    }
                    location.href = '/U/Profile?Info'
                } else if (Status == '409') {
                    MessageCreateForm.querySelector('p').innerText = 'نام کاربری انتخاب شده از قبل وجود دارد '
                    MessageCreateForm.classList.remove('ContainerMessageSuccess')
                    MessageCreateForm.classList.add('ContainerMessageError')
                } else if (Status == '204') {
                    MessageCreateForm.querySelector('p').innerText = ' لطفا فیلد هارا پر نمایید'
                    MessageCreateForm.classList.remove('ContainerMessageSuccess')
                    MessageCreateForm.classList.add('ContainerMessageError')
                }
            })
        }
