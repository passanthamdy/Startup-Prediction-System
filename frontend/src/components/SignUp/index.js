import React, { useState } from 'react';
import axiosInstance from '../../axiosInstance';
import { useHistory } from 'react-router-dom';

//matrial 
import logo from '../../images/logo.png'
import { Container, Form, FormButton, FormContent, FormH1, FormInput, FormLabel, FormWrap, Icon, Text, TextR } from './SignUpElements'

const SignUp = () => {
    const history = useHistory();

    //A frozen object can no longer be changed
	const initialFormData = Object.freeze({
		email: '',
		username: '',
		password: '',
	});

    const [formData, setFormData] = useState(initialFormData);

	const handleChange = (e) => {
		setFormData({
			...formData,
			// Trimming any whitespace
			[e.target.name]: e.target.value.trim(),
		});
	};
    

    const handleSubmit = (e) => {
		e.preventDefault();
		console.log(formData);

		axiosInstance
			.post(`accounts/users/create/`, {
				email: formData.email,
				user_name: formData.username,
				password: formData.password,
			})
			.then( res => {
                console.log('res')
                history.push('/');
			})
            .catch((error) =>{
                console.log('error', error.response.data)
            });
	};
    return (
        <>
             <Container>
                 <FormWrap>
                    <FormContent>
                        <Form >
                            <FormH1>Sign in to your account</FormH1>
                            <FormLabel htmlFor='for'>User Name</FormLabel>
                            <FormInput type="text" required name="username" onChange={handleChange}/>
                            <FormLabel htmlFor='for'>Email</FormLabel>
                            <FormInput type="email" name="email" required onChange={handleChange} />
                            <FormLabel htmlFor='for'>Password</FormLabel>
                            <FormInput type="password" required name="password" onChange={handleChange}/>
                            <FormButton type='submit' onClick={handleSubmit}>Continue</FormButton><br/>
                            <Text>ALready have an account ?<TextR to="/signin">Sign in</TextR></Text>
                        </Form>
                    </FormContent>
                 </FormWrap>
             </Container>
        </>
    )
}

export default SignUp