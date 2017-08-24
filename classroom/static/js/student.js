/*<div class="table" style="background-color:#333333; display:none">
<div class="row">
    <div class="col-md-offset-3 col-md-6">
        <table class="table course-table" style="display:none">*/

$(document).ready(function(){

    $(".my-courses").click(function(){

       
        //gets first number in url like student/id/courses
        function getUrlId(){
        var path  = window.location.pathname;
        var result = path.match('[\\d]+');  
        return result[0];
        };
        page_id =  getUrlId()

        $("div.table").show()
        var table = $("table.course-table");
        table.addClass('table-striped table-condensed table-bordered')

         if(table.attr('on') == 'true'){
            table.attr('on', 'false')
            table.hide()
            $("div.table").hide()
            table.remove()

        }

        else{
        $("div.table").show()
        table.attr('on', 'true')
        }

        $.ajax({
        method: "GET",
        url: "/student/" + page_id + "/courses",
        contentType: "application/json",
        dataType: 'json',

        })
        .done(function(courses) {
            result = courses
            //access to dictionary 
            //result['courses'] = [{course1:ejrkedlejdl}, {course2:eljkrje}] a list
            //console.log(result['courses'][0]['id'])
            course_list = result['courses']
            console.log(result['courses'][0])
            console.log(course_list[0]['name'])
            var i = 1

         //result is a reference to courses (a dictionary with key 'courses': value - list of 3 course objects)
          for(course in course_list){
                var table_row = $("<tr/>").css('background-color','white')
                path = '/courses/'
                var url = $('<a/>').attr('href', path + (course_list[course]['id']))
                url.text(course_list[course]['name'])
                $("<td/>").text(i).appendTo(table_row)
                $("<td/>").append(url).appendTo(table_row)
                $("<td/>").text(course_list[course]['category']).appendTo(table_row)
                $("<td/>").text(course_list[course]['difficulty']).appendTo(table_row)
                $("<td/>").text(course_list[course]['start_date']).appendTo(table_row)
                $("<td/>").text(course_list[course]['limit']).appendTo(table_row)
                table_row.appendTo($(".course-table tbody"))
                i+=1;
            }

              table.show()
          
       })
    })
})

$(document).ready(function(){

        $(".add-course").click(function(){
            $("div.inner-table").hide()

            var form = $('add-course-form')
            if(form.attr('on') == 'off'){
                form.show()

            }

            else{
                form.hide()
            }
            
        })



})
    
