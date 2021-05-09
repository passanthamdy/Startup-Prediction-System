import React, {useState} from 'react'
import SubNavbar from '../components/SubNav';
import SubSide from '../components/SubSide'

const InvestorsPage = () => {
    const[isOpen, setIsOpen] = useState(false);

    const toggle = () => {
        setIsOpen(!isOpen)
    }
    return (
        <>
          
          <SubNavbar toggle={toggle}/>
          <SubSide isOpen = {isOpen} toggle= {toggle}/>
          <h1>investors</h1>
          
        </>
    )
}

export default InvestorsPage