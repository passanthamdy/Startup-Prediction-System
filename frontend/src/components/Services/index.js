import React from 'react'

const Services = () => {
    return (
        <ServicesContainer id="services">
            <ServicesH1>Our Services</ServicesH1>
            <ServicesWrapper>
                <ServicesCard>
                    <ServicesIcon src={icon1}/>
                    <ServicesH2>Publish your idea</ServicesH2>
                    <ServicesP>We help publish your idea with no fee.</ServicesP>
                </ServicesCard>
                <ServicesCard>
                    <ServicesIcon src={icon2}/>
                    <ServicesH2>Find your chances to succeed</ServicesH2>
                    <ServicesP>We help you to find the exact percentage of how your startup will succeed</ServicesP>
                </ServicesCard>
                <ServicesCard>
                    <ServicesIcon src={icon3}/>
                    <ServicesH2>For investors</ServicesH2>
                    <ServicesP>We help you to know where to put your money and why.</ServicesP>
                </ServicesCard>
            </ServicesWrapper>
        </ServicesContainer>
    )
}

export default Services
