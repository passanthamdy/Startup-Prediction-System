import React from 'react';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';

export default function DescForm() {
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
    </React.Fragment>
  );
}