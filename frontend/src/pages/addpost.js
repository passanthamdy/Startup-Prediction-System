import React, {useState} from 'react'
import ScrollToTop from '../components/ScrollToTop';
import SubNavbar from '../components/SubNav';
import SubSide from '../components/SubSide'
import Checkout from '../components/CreatePost'

const AddPostsPage = () => {
    const[isOpen, setIsOpen] = useState(false);

    const toggle = () => {
        setIsOpen(!isOpen)
    }
    return (
        <>
          <ScrollToTop />
          <SubNavbar toggle={toggle}/>
          <SubSide isOpen = {isOpen} toggle= {toggle}/>
          <Checkout />
        </>
    )
}

export default AddPostsPage
