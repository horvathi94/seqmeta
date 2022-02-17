const gulp = require("gulp");
const sass = require("gulp-sass")(require("sass"));
const autoprefixer = require("gulp-autoprefixer");
const cssmin = require("gulp-cssmin");
const rename = require("gulp-rename");
const uglify = require("gulp-uglify");


static_dir = "web-interface/app/app/static/";


gulp.task("styles", function(){

	return gulp.src("./dev/scss/*scss")
		.pipe(sass().on("error", sass.logError))
		.pipe(autoprefixer())
		.pipe(cssmin())
		.pipe(rename({sufix: ".min"}))
		.pipe( gulp.dest(static_dir+"css") );

});


gulp.task("js", function(){
	
	return gulp.src("./dev/js/*.js")
		.pipe(uglify())
		.pipe(gulp.dest(static_dir+"js"));

});


gulp.task("watch:styles", function () {
    return gulp.watch("./dev/scss/*.scss", gulp.series("styles"));
});


gulp.task("watch:js", function() {
	return gulp.watch("./dev/js/*.js", gulp.series("js"));
});


gulp.task("default", gulp.parallel("watch:js", "watch:styles"));
