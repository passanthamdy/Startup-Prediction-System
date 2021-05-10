import React from 'react'
import {animateScroll as scroll} from 'react-scroll'
import {
    FooterContainer,
    FooterLink,
    FooterLinkTitle,
    FooterWrap,
    FooterLinksContainer,
    FooterLinksWrapper,
    FooterLinksItems,
    SocialMedia,
    SocialMediaWrap,
    SocialLogo,
    WebsiteRights,
    SocialIcons,
    SocialIconLinks

} 
from './FooterElements'
import logo from '../../images/logo.png'
import { FaFacebook, FaGithub, FaInstagram, FaTwitch, FaTwitter } from 'react-icons/fa'
const toggleHome = () =>{
    scroll.scrollToTop();
}
const Footer = () => {
    return (
        <FooterContainer>
            <FooterWrap>
                <FooterLinksContainer>
                    <FooterLinksWrapper>
                        <FooterLinksItems>
                            <FooterLinkTitle>About Us</FooterLinkTitle>
                                
                                <FooterLink to="/signin">Team members</FooterLink>
                                <FooterLink to="/signin">Terms of services</FooterLink>
                            
                        </FooterLinksItems>
                        <FooterLinksItems>
                            <FooterLinkTitle>Contact Us</FooterLinkTitle>
                                
                                <FooterLink to="/signin">Contact</FooterLink>
                                <FooterLink to="/signin">Support</FooterLink>
                            
                        </FooterLinksItems>
                        <FooterLinksItems>
                            <FooterLinkTitle>Startups</FooterLinkTitle>
                                
                                <FooterLink to="/posts">Post a startup</FooterLink>
                                <FooterLink to="/posts">All startups</FooterLink>
                                <FooterLink to="/investors">All investors</FooterLink>
                                
                            
                        </FooterLinksItems>
                    </FooterLinksWrapper>
                </FooterLinksContainer>
                <SocialMedia>
                    <SocialMediaWrap>
                        <SocialLogo to='/' onClick={toggleHome}>
                            <img src={logo} alt="logo"></img>
                        </SocialLogo>
                        <WebsiteRights>Startupista © {new Date().getFullYear()} All rights reserved. </WebsiteRights>
                        <SocialIcons> 
                            <SocialIconLinks href="https://www.facebook.com/" target="_blank" aria-label="Facebook"><FaFacebook/></SocialIconLinks>
                            <SocialIconLinks href="https://github.com/yusseef" target="_blank" aria-label="Github"><FaGithub/></SocialIconLinks>
                            <SocialIconLinks href="https://www.instagram.com/" target="_blank" aria-label="Instagram"><FaInstagram/></SocialIconLinks>
                            <SocialIconLinks href="https://www.twitter.com/" target="_blank" aria-label="Twitter"><FaTwitter/></SocialIconLinks>
                        </SocialIcons>
                    </SocialMediaWrap>
                </SocialMedia>
            </FooterWrap>
        </FooterContainer>
    )
}

export default Footer
