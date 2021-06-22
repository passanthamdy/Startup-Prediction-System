import React, {useState} from 'react'
import ScrollToTop from '../components/ScrollToTop';
import SubNavbar from '../components/SubNav';
import SubSide from '../components/SubSide'
import {Button} from '../components/ButtonElements'
import Posts from '../components/Posts'
const PostsPage = () => {
    const[isOpen, setIsOpen] = useState(false);

    const toggle = () => {
        setIsOpen(!isOpen)
    }
    return (
        <>
        <ScrollToTop />
        <SubNavbar toggle={toggle}/>
        <SubSide isOpen = {isOpen} toggle= {toggle}/>
        <br />
        <Posts />
          
        </>
    )
}

export default PostsPage
