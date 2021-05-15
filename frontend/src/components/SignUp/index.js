import React, { useState } from "react";
import axiosInstance from "../../axiosInstance";
import { useHistory } from "react-router-dom";
import { useFormik } from "formik";
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
} from "./SignUpElements";

const initialValues = {
  email: "",
  username: "",
  password: "",
};

const SignUp = () => {
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
        console.log("error", error.response.data);
      });
  };
  const formik = useFormik({
    initialValues,
    onSubmit,
    validate,
  });

  
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
              <FormH1>Sign in to your account</FormH1>
              <FormLabel htmlFor="for">User Name</FormLabel>
              <FormInput
                type="text"
                name="username"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.username}
              />
              {formik.touched.username && formik.errors.username ? (
                <div className="error">{formik.errors.username}</div>
              ) : null}
              <FormLabel htmlFor="for">Email</FormLabel>
              <FormInput
                type="email"
                name="email"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.email}
              />
              {formik.touched.email && formik.errors.email ? (
                <div className="error">{formik.errors.email}</div>
              ) : null}

              <FormLabel htmlFor="for">Password</FormLabel>
              <FormInput
                type="password"
                name="password"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.password}
              />
              {formik.touched.password && formik.errors.password ? (
                <div className="error">{formik.errors.password}</div>
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
