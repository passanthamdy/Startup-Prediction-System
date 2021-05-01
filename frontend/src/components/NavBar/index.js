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
     NavBtn
    }
     from './NavbarElements'



const Navbar = ({toggle}) => {
    return (
        <>
        <Nav>
            <NavbarContainer>
                <NavLogo to='/'><img src={logo}></img></NavLogo>
                <MobileIcon onClick= {toggle}>
                    <FaBars />
                </MobileIcon>
                <NavMenu> 
                    <NavItems>
                        <NavLinks to='about'>about</NavLinks>
                    </NavItems>
                    <NavItems>
                        <NavLinks to='startups'>Startups</NavLinks>
                    </NavItems>
                    <NavItems>
                        <NavLinks to='investors'>Investors</NavLinks>
                    </NavItems>
                    <NavItems>
                        <NavLinks to='signup'>Signup</NavLinks>
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

export default Navbar
