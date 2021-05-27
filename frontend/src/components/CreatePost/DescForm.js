import React from 'react';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import PhotoCamera from '@material-ui/icons/PhotoCamera';
const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(0),
      width: 500,
    },
  },
  input: {
    display: 'none',
  },
}));
export default function DescForm() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Typography variant="h6" gutterBottom>
        Description
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} md={600}>
          <TextField required id="Desc" label="Short description" fullWidth autoComplete="cc-name" multiline />
        </Grid>
        <Grid item xs={12} md={600}>
          <TextField required id="FullDesc" label="Description" fullWidth autoComplete="cc-name" rows={10} multiline />
        </Grid>
      </Grid>
      <br />
      <Typography variant="h6" gutterBottom>
        Upload startup photo
      </Typography>
      <div className={classes.root}>
      <input accept="image/*" className={classes.input} id="icon-button-file" type="file" />
      <label htmlFor="icon-button-file">
        <IconButton color="primary" aria-label="upload picture" component="span">
          <PhotoCamera />
        </IconButton>
      </label>
    </div>
    </React.Fragment>
  );
}