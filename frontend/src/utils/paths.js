import AccountList from "../pages/AccountList/AccountList";
import AccountPage from "../pages/AccountPage/AccountPage";
import ApplicationList from "../pages/ApplicationList/ApplicationList";
import HomePage from "../pages/HomePage/HomePage";
import LoginPage from "../pages/LoginPage/LoginPage";
import LogoutPage from "../pages/LogoutPage/LogoutPage";
import RegisterPage from "../pages/RegisterPage/RegisterPage";
import UpdateApplication from "../pages/UpdateApplication/UpdateApplication";

const paths = [
    {path: '/register', component: RegisterPage, name: 'Register', exact: true},
    {path: '/login', component: LoginPage, name: 'Login', exact: true},
    {path: '/account', component: AccountPage, name: 'Account', exact: true},
    {path: '/logout', component: LogoutPage, name: 'Logout', exact: true},
    {path: '/', component: HomePage, name: 'Home', exact: true,},

    
    {path: '/applications', component: ApplicationList, name: 'Applications', exact: true,},
    {path: '/userlist', component: AccountList, name: 'Accounts', exact: true,},

    {path: '/application/:id', component: UpdateApplication, name: 'DetailProject', exact: true},
  ];

export default paths;