function showExperience()
    {
            document.getElementById("Detail1").innerHTML = 
            'Training coordinator at combat squadron (Outstanding soldier award)<br>\n'+
            '• Planning and executing training programs as required<br>\n' +
            '• Orchestrate and coordinate all the squadrons flight training, reserve, and secure light zones and paths through IAF headquarters.<br>\n'+
            '• Partnership in the decision-making process as part of the executive staff<br>\n' +
            '• Responsible for the operational competence and adjustment of the unitsmembers.<br>\n' + '<br>\n'+

            'Training coordinator at combat squadron (Outstanding soldier award)<br>\n'+
            '• Managing the operations of the control room for routine work and in emergency situations, in great detail and with responsibility<br>\n' +
            '• The job required to comply with high pressures, tight schedule and teamwork.<br>\n'+
            '• Assemble and analyze data from multiple sources.<br>\n'
            ;
    }

    function showSkills()
    {
        document.getElementById("Detail2").innerHTML =
        '• Microsoft Office competency (Office: Excel, Word, PowerPoint)<br>\n' + 
        '• Power BI<br>\n' + 
        '• Tableau<br>\n' + 
        '• Programming Languages: Java (main), Python, VBA, SQL, RStudio<br>\n';
       }


       function validateEmail() {
        var emailID = document.ContactForm.EMail.value;
        atpos = emailID.indexOf("@");
        dotpos = emailID.lastIndexOf(".");
        
        if (atpos < 1 || ( dotpos - atpos < 2 )) {
           alert("Please enter correct email ID")
           document.myForm.EMail.focus() ;
           return false;
        }
        return( true );
     }