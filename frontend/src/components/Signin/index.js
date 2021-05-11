import React from 'react'
import logo from '../../images/logo.png'
import { Container, Form, FormButton, FormContent, FormH1, FormInput, FormLabel, FormWrap, Icon, Text, TextR } from './SigninElements'
import {Link} from 'react-router-dom';
const SignIn = () => {
    return (
        <>
             <Container>
                 <FormWrap>
                    <FormContent>
                        <Form action="#">
                            <FormH1>Sign in to your account</FormH1>
                            <FormLabel htmlFor='for'>Email</FormLabel>
                            <FormInput type="email" required />
                            <FormLabel htmlFor='for'>Password</FormLabel>
                            <FormInput type="password" required />
                            <FormButton type='submit'>Continue</FormButton><br/>
                            <Text>Dont have an account ?<TextR to="/signup">Sign up</TextR></Text>
                        </Form>
                    </FormContent>
                 </FormWrap>
             </Container>
        </>
    )
}

export default SignIn