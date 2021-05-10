import React, {useState, useEffect} from 'react'
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
     from './NavbarElements'



const Navbar = ({toggle}) => {
    const [scrollNav, setScrollNav] = useState(false);

    const changeNav = () => {
        if(window.scrollY >= 80){
            setScrollNav(true)
        } else{
            setScrollNav(false)
        }
    }
    useEffect(() => {
        window.addEventListener('scroll', changeNav)
    }, [])

    return (
        <>
        <Nav scrollNav={scrollNav}>
            <NavbarContainer>
                <NavLogo to='/'><img src={logo} alt="logo"></img></NavLogo>
                <MobileIcon onClick= {toggle}>
                    <FaBars />
                </MobileIcon>
                <NavMenu> 
                    <NavItems>
                        <NavLinks to='about'>About</NavLinks>
                    </NavItems>
                    <NavItems>
                        <NavLinks to='discover'>Discover</NavLinks>
                    </NavItems>
                    <NavItems>
                        <NavLinks to='services'>Services</NavLinks>
                    </NavItems>
                    <NavItems>
                        <NavLinksR to='/posts'>Startups</NavLinksR>
                    </NavItems>
                    <NavItems>
                        <NavLinksR to='/investors'>Investors</NavLinksR>
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
