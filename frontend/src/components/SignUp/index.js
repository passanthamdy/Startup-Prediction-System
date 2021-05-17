import React, { useEffect, useState } from "react";
import axiosInstance from "../../axiosInstance";
import { useHistory } from "react-router-dom";
import { Formik, useFormik } from "formik";
import Container from "react-bootstrap/Container";
import validate from "./validation";
//matrial
import logo from "../../images/logo.png";
import {
  Form,
  FormButton,
  FormContent,
  FormH1,
  FormInput,
  FormLabel,
  FormWrap,
  Icon,
  Text,
  TextR,
  Error,
} from "./SignUpElements";

const initialValues = {
  email: "",
  username: "",
  password: "",
};

const SignUp = () => {
  const [emailError, setEmailError] = useState([]);
  const [userNameError, setUserNameError] = useState([]);
  const history = useHistory();
  const onSubmit = (values) => {
    console.log(values);
    axiosInstance
      .post("accounts/users/create/", {
        email: values.email,
        user_name: values.username,
        password: values.password,
      })
      .then((res) => {
        console.log("res", res);
        history.push("/");
      })
      .catch((error) => {
        if (error.response.data.email) setEmailError(error.response.data.email);
        if (error.response.data.user_name)
          setUserNameError(error.response.data.user_name);
        console.log("error", error.response.data);
      });
  };
  const formik = useFormik({
    initialValues,
    onSubmit,
    validate,
  });

  useEffect(() => {
    //check email
  }, [formik.values.email]);

  useEffect(() => {
    //check username
  }, [formik.values.username]);
  return (
    <>
      <Container
        style={{
          background:
            "linear-gradient(108deg, rgba(0,0,0,1)0% , rgba(220, 161, 255, 1)100%)",
        }}
      >
        <Icon to="/">
          <img src={logo} alt="logo"></img>
        </Icon>
        <FormWrap>
          <FormContent>
            <Form onSubmit={formik.handleSubmit}>
              <FormH1>Sign up your account</FormH1>
              {emailError.length > 0 && !formik.errors.email ? (
                <Error>{emailError}</Error>
              ) : null}
              {userNameError.length > 0 && !formik.errors.username ? (
                <Error>{userNameError}</Error>
              ) : null}
              <FormLabel htmlFor="for">User Name</FormLabel>
              <FormInput
                type="text"
                name="username"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.username}
              />
              {formik.touched.username &&
              formik.errors.username &&
              formik.values.username.length > 0 ? (
                <Error className="error">{formik.errors.username}</Error>
              ) : null}
              <FormLabel htmlFor="for">Email</FormLabel>
              <FormInput
                type="email"
                name="email"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.email}
              />
              {formik.touched.email &&
              formik.errors.email &&
              formik.values.email.length > 0 ? (
                <Error className="error">{formik.errors.email}</Error>
              ) : null}

              <FormLabel htmlFor="for">Password</FormLabel>
              <FormInput
                type="password"
                name="password"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.password}
              />
              {formik.touched.password &&
              formik.errors.password &&
              formik.values.password.length > 0 ? (
                <Error className="error">{formik.errors.password}</Error>
              ) : null}

              <FormButton type="submit">Continue</FormButton>
              <br />
              <Text>
                ALready have an account ?<TextR to="/signin">Sign in</TextR>
              </Text>
            </Form>
          </FormContent>
        </FormWrap>
      </Container>
    </>
  );
};

export default SignUp;
