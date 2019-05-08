# Publishing on COMP

This guide describes how to publish a model on COMP. The COMP framework depends on model interfaces meeting several COMP criteria, and we walk you through how to meet those criteria, either by modifying your model's interface or building a new wrapper interface around your model. The great part is that you don't have to deal with any web technology to build your COMP app.

If you have any questions as you proceed through this guide, send Hank an email at henrymdoupe@gmail.com.

The documentation is split into three parts. 

- The first part documents the [inputs](/publish/inputs) and [outputs](/publish/outputs/) JSON schemas that your model will need to adopt for COMP to be able to generate input forms representing your model's default specification, validate user adjustments, and display model outputs. 
- The [second part](/publish/endpoints/) documents the python functions that will be used by COMP to get data from and submit data to your model. 
- The third part is a [publish form](https://www.compmodels.org/publish) that asks you to provide a title and overview for your new COMP app, code snippets for the three python functions, and information describing your app's resource requirements and installation directions. If you would like to see a publishing template that has already been completed, you can view the Matchups template [here](https://www.compmodels.com/hdoupe/Matchups/detail).

Once you've submitted the publishing form, Hank will review it and get back to you within 24 hours to inform you whether the model is ready to be published or if there are criteria that have not been satisfied. Your model will be deployed to COMP once it has met all of the critera. You will have the opportunity to test it out after it has been deployed.