import React , {useState} from 'react'
import axiosInstance from '../../axiosInstance';
import { useHistory } from 'react-router-dom';
//matrial
import logo from '../../images/logo.png'
import { Container, Form, FormButton, FormContent, FormH1, FormInput, FormLabel, FormWrap, Icon, Text, TextR } from './SigninElements'


const SignIn = () => {
    const history = useHistory();
	const initialFormData = Object.freeze({
		email: '',
		password: '',
	});

	const [formData, setFormData] = useState(initialFormData);

	const handleChange = (e) => {
		setFormData({
			...formData,
			[e.target.name]: e.target.value.trim(),
		});
	};

    const handleSubmit =(e) => {
        e.preventDefault();

        axiosInstance .post('/accounts/token/obtain/',
        {
            email:formData.email,
            password:formData.password
        })
        .then((res) => {
            localStorage.setItem('access_token', res.data.access);
            localStorage.setItem('refresh_token', res.data.refresh);
            axiosInstance.defaults.headers['Authorization'] =
                'JWT ' + localStorage.getItem('access_token');
            history.push('/posts');
            //console.log(res);
            //console.log(res.data);
        })
        .catch((err)=>{
            console.log(err)
        })

    };

    return (
        <>
             <Container>
                 <FormWrap>
                 <Icon to="/"><img src={logo} alt="logo"></img></Icon>
                    <FormContent>
                        <Form >
                            <FormH1>Sign in to your account</FormH1>
                            <FormLabel htmlFor='for'>Email</FormLabel>
                            <FormInput type="email" required  name="email" onChange={handleChange}/>
                            <FormLabel htmlFor='for'>Password</FormLabel>
                            <FormInput type="password" required name="password" onChange={handleChange}/>
                            <FormButton type='submit' onClick={handleSubmit}> Continue</FormButton><br/>
                            <Text>Dont have an account ?<TextR to="/signup">Sign up</TextR></Text>
                        </Form>
                    </FormContent>
                 </FormWrap>
             </Container>
        </>
    )
}

export default SignIn