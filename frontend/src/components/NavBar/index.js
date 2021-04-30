import React from 'react'
import {Nav, NavbarContainer, NavLogo} from './NavbarElements'


const Navbar = () => {
    return (
        <>
        <Nav>
            <NavbarContainer>
                <NavLogo to='/'>S</NavLogo>
                <MobileIcon>
                    <FaBars />
                </MobileIcon>
                <NavMenu> 
                    <NavItems>
                        <NavLinks to='about'>about</NavLinks>
                    </NavItems>
                </NavMenu>
            </NavbarContainer>
        </Nav>
        </>
    )
}

export default Navbar
