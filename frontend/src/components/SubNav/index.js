import React from 'react'
import {FaBars} from 'react-icons/fa'
import logo from '../../images/logo.png'
import {
     Nav,
     NavbarContainer,
     NavLogo,
     MobileIcon, 
     NavMenu, 
     NavItems, 
     NavLinks,
     NavBtnLink,
     NavBtn, 
     NavLinksR
    }
     from './SubnavElements'



const SubNavbar = ({toggle}) => {
    return (
        <>
        <Nav>
            <NavbarContainer>
                <NavLogo to='/'><img src={logo} alt="logo"></img></NavLogo>
                <MobileIcon onClick= {toggle}>
                    <FaBars />
                </MobileIcon>
                <NavMenu> 
                    <NavItems>
                        <NavLinks to='/'>Home</NavLinks>
                    </NavItems>
                    <NavItems>
                        <NavLinks to='/posts'>Startups</NavLinks>
                    </NavItems>
                    <NavItems>
                        <NavLinks to='/investors'>Investors</NavLinks>
                    </NavItems>
                    <NavItems>
                        <NavLinks to='/signup'>Signup</NavLinks>
                    </NavItems>
                    
                </NavMenu>
                <NavBtn>
                    <NavBtnLink to='/signin'>Sign in</NavBtnLink>
                </NavBtn>
            </NavbarContainer>
        </Nav>
        </>
    )
}

export default SubNavbar
