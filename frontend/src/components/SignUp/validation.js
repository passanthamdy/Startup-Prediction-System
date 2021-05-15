const validate = values => {
  const errors = {};
  if (!values.username) {
    errors.username = "Username Required";
  } else if (values.username.length < 5) {
    errors.username = "Username must be at least 5 characters";
  }
  if (!values.password) {
    errors.password = "Password Required";
  }
  if (!values.email) {
    errors.email = "Required";
  } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)) {
    errors.email = "Invalid email address";
  }

  return errors;
};
export default validate;
