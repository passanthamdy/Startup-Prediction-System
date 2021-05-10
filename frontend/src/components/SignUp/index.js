import React from 'react'
import logo from '../../images/logo.png'
import { Container, Form, FormButton, FormContent, FormH1, FormInput, FormLabel, FormWrap, Icon, Text, TextR } from './SignUpElements'
import {Link} from 'react-router-dom';
const SignUp = () => {
    return (
        <>
             <Container>
                 <FormWrap>
                    <Icon to="/"><img src={logo} alt="logo"></img></Icon>
                    <FormContent>
                        <Form action="#">
                            <FormH1>Sign in to your account</FormH1>
                            <FormLabel htmlFor='for'>Name</FormLabel>
                            <FormInput type="text" required />
                            <FormLabel htmlFor='for'>Email</FormLabel>
                            <FormInput type="email" required />
                            <FormLabel htmlFor='for'>Password</FormLabel>
                            <FormInput type="password" required />
                            <FormButton type='submit'>Continue</FormButton><br/>
                            <Text>ALready have an account ?<TextR to="/signin">Sign in</TextR></Text>
                        </Form>
                    </FormContent>
                 </FormWrap>
             </Container>
        </>
    )
}

export default SignUp