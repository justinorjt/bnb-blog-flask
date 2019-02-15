(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"],{

/***/ "./src/$$_lazy_route_resource lazy recursive":
/*!**********************************************************!*\
  !*** ./src/$$_lazy_route_resource lazy namespace object ***!
  \**********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncaught exception popping up in devtools
	return Promise.resolve().then(function() {
		var e = new Error("Cannot find module '" + req + "'");
		e.code = 'MODULE_NOT_FOUND';
		throw e;
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "./src/$$_lazy_route_resource lazy recursive";

/***/ }),

/***/ "./src/app/app-routing.module.ts":
/*!***************************************!*\
  !*** ./src/app/app-routing.module.ts ***!
  \***************************************/
/*! exports provided: AppRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppRoutingModule", function() { return AppRoutingModule; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _landingpage_landingpage_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./landingpage/landingpage.component */ "./src/app/landingpage/landingpage.component.ts");
/* harmony import */ var _page_not_found_page_not_found_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./page-not-found/page-not-found.component */ "./src/app/page-not-found/page-not-found.component.ts");
/* harmony import */ var _blog_post_form_blog_post_form_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./blog-post-form/blog-post-form.component */ "./src/app/blog-post-form/blog-post-form.component.ts");






var routes = [
    { path: '', component: _landingpage_landingpage_component__WEBPACK_IMPORTED_MODULE_3__["LandingpageComponent"] },
    { path: 'home', component: _landingpage_landingpage_component__WEBPACK_IMPORTED_MODULE_3__["LandingpageComponent"] },
    { path: 'blog-post-form', component: _blog_post_form_blog_post_form_component__WEBPACK_IMPORTED_MODULE_5__["BlogPostFormComponent"] },
    // { path: 'investor', loadChildren: '@app/investor/investor.module#InvestorModule' },
    // { path: 'sponsor', loadChildren: '@app/sponsor/sponsor.module#SponsorModule' },
    // { path: 'auditor', loadChildren: '@app/auditor/auditor.module#AuditorModule' },
    // { path: 'contractor', loadChildren: '@app/contractor/contractor.module#ContractorModule' },
    // { path: 'subcontractor', loadChildren: '@app/subcontractor/subcontractor.module#SubcontractorModule' },
    // { path: 'auth', loadChildren: '@app/auth/auth.module#AuthModule' },
    { path: '', redirectTo: '/home', pathMatch: 'full' },
    { path: '404', component: _page_not_found_page_not_found_component__WEBPACK_IMPORTED_MODULE_4__["PageNotFoundComponent"] },
    { path: '**', redirectTo: '/404' },
];
var AppRoutingModule = /** @class */ (function () {
    function AppRoutingModule() {
    }
    AppRoutingModule = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"])({
            imports: [
                _angular_router__WEBPACK_IMPORTED_MODULE_2__["RouterModule"].forRoot(routes),
            ],
            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_2__["RouterModule"]]
        })
    ], AppRoutingModule);
    return AppRoutingModule;
}());



/***/ }),

/***/ "./src/app/app.component.css":
/*!***********************************!*\
  !*** ./src/app/app.component.css ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".inner{\r\n\tflex: 1 1 auto;\r\n\talign-self: stretch;\t\r\n}\r\n\r\n.content-wrapper{\r\n\twidth: 100%;\r\n\tmin-height: 100vh;\r\n\toverflow: hidden;\r\n\t/*transition: .5s;*/\r\n}\r\n\r\n#wrapper{\r\n\theight: 100vh;\r\n}\r\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvYXBwLmNvbXBvbmVudC5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7Q0FDQyxlQUFlO0NBQ2Ysb0JBQW9CO0NBQ3BCOztBQUVEO0NBQ0MsWUFBWTtDQUNaLGtCQUFrQjtDQUNsQixpQkFBaUI7Q0FDakIsb0JBQW9CO0NBQ3BCOztBQUVEO0NBQ0MsY0FBYztDQUNkIiwiZmlsZSI6InNyYy9hcHAvYXBwLmNvbXBvbmVudC5jc3MiLCJzb3VyY2VzQ29udGVudCI6WyIuaW5uZXJ7XHJcblx0ZmxleDogMSAxIGF1dG87XHJcblx0YWxpZ24tc2VsZjogc3RyZXRjaDtcdFxyXG59XHJcblxyXG4uY29udGVudC13cmFwcGVye1xyXG5cdHdpZHRoOiAxMDAlO1xyXG5cdG1pbi1oZWlnaHQ6IDEwMHZoO1xyXG5cdG92ZXJmbG93OiBoaWRkZW47XHJcblx0Lyp0cmFuc2l0aW9uOiAuNXM7Ki9cclxufVxyXG5cclxuI3dyYXBwZXJ7XHJcblx0aGVpZ2h0OiAxMDB2aDtcclxufSJdfQ== */"

/***/ }),

/***/ "./src/app/app.component.html":
/*!************************************!*\
  !*** ./src/app/app.component.html ***!
  \************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"content-wrapper d-flex flex-column\">\n  <app-header></app-header>\n\n    <div class=\"container-fluid h-100 inner mb-4\">\n      <router-outlet></router-outlet>\n    </div>\n  <app-footer></app-footer>\n</div>\n"

/***/ }),

/***/ "./src/app/app.component.ts":
/*!**********************************!*\
  !*** ./src/app/app.component.ts ***!
  \**********************************/
/*! exports provided: AppComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppComponent", function() { return AppComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var AppComponent = /** @class */ (function () {
    function AppComponent() {
        this.title = 'AirBNB-blog';
    }
    AppComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-root',
            template: __webpack_require__(/*! ./app.component.html */ "./src/app/app.component.html"),
            styles: [__webpack_require__(/*! ./app.component.css */ "./src/app/app.component.css")]
        })
    ], AppComponent);
    return AppComponent;
}());



/***/ }),

/***/ "./src/app/app.module.ts":
/*!*******************************!*\
  !*** ./src/app/app.module.ts ***!
  \*******************************/
/*! exports provided: AppModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppModule", function() { return AppModule; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/platform-browser */ "./node_modules/@angular/platform-browser/fesm5/platform-browser.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./app.component */ "./src/app/app.component.ts");
/* harmony import */ var _app_routing_module__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./app-routing.module */ "./src/app/app-routing.module.ts");
/* harmony import */ var _ui_ui_module__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./ui/ui.module */ "./src/app/ui/ui.module.ts");
/* harmony import */ var _landingpage_landingpage_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./landingpage/landingpage.component */ "./src/app/landingpage/landingpage.component.ts");
/* harmony import */ var _page_not_found_page_not_found_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./page-not-found/page-not-found.component */ "./src/app/page-not-found/page-not-found.component.ts");
/* harmony import */ var _blog_post_form_blog_post_form_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./blog-post-form/blog-post-form.component */ "./src/app/blog-post-form/blog-post-form.component.ts");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");










var AppModule = /** @class */ (function () {
    function AppModule() {
    }
    AppModule = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_2__["NgModule"])({
            declarations: [
                _app_component__WEBPACK_IMPORTED_MODULE_3__["AppComponent"],
                _landingpage_landingpage_component__WEBPACK_IMPORTED_MODULE_6__["LandingpageComponent"],
                _page_not_found_page_not_found_component__WEBPACK_IMPORTED_MODULE_7__["PageNotFoundComponent"],
                _blog_post_form_blog_post_form_component__WEBPACK_IMPORTED_MODULE_8__["BlogPostFormComponent"]
            ],
            imports: [
                _angular_platform_browser__WEBPACK_IMPORTED_MODULE_1__["BrowserModule"],
                _ui_ui_module__WEBPACK_IMPORTED_MODULE_5__["UiModule"],
                _angular_forms__WEBPACK_IMPORTED_MODULE_9__["FormsModule"],
                _app_routing_module__WEBPACK_IMPORTED_MODULE_4__["AppRoutingModule"],
            ],
            providers: [],
            bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_3__["AppComponent"]]
        })
    ], AppModule);
    return AppModule;
}());



/***/ }),

/***/ "./src/app/blog-post-form/blog-post-form.component.css":
/*!*************************************************************!*\
  !*** ./src/app/blog-post-form/blog-post-form.component.css ***!
  \*************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2Jsb2ctcG9zdC1mb3JtL2Jsb2ctcG9zdC1mb3JtLmNvbXBvbmVudC5jc3MifQ== */"

/***/ }),

/***/ "./src/app/blog-post-form/blog-post-form.component.html":
/*!**************************************************************!*\
  !*** ./src/app/blog-post-form/blog-post-form.component.html ***!
  \**************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"container-fluid d-flex justify-content-center my-2\">\n\t<div class=\"col-md-10\">\n\t\t<div class=\"card\">\n\t\t\t<div class=\"card-header text-center\">\n\t\t\t\t<h4>Blog Post Form</h4>\n\t\t\t\t\n\t\t\t</div>\n\t\t\t<div class=\"card-body\">\n\t\t\t\t<form (submit)='SubmitPost($event)'>\n\t\t\t\t\t<div class=\"form-group col-md-9\">\n\t\t\t\t\t\t<label>Header</label>\n\t\t\t\t\t\t<input class=\"form-control\" type=\"text\" id=\"header\" placeholder=\"Main Headline\">\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class=\"form-group col-md-9\">\n\t\t\t\t\t\t<label>Sub-Header</label>\n\t\t\t\t\t\t<input class=\"form-control\" type=\"text\" id=\"subheader\" placeholder=\"Extra Details\">\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class=\"form-group col-md-9\">\n\t\t\t\t\t\t<label>Author</label>\n\t\t\t\t\t\t<input class=\"form-control\" type=\"text\" id=\"author\" placeholder=\"Jane Smith\">\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class=\"form-group col-md-12\">\n\t\t\t\t\t\t<label>Content</label>\n\t\t\t\t\t\t<textarea rows=\"9\" class=\"form-control\" id=\"content\" placeholder=\"Write your blog content here\"></textarea>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class=\"form-group col-md-9\">\n\t\t\t\t\t\t<label>Hashtags</label>\n\t\t\t\t\t\t<input class=\"form-control\" type=\"text\" id=\"hashtags\" placeholder=\"Separate by comma: (fun, happy, food, rent) \">\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class=\"form-group col-md-9\">\n\t\t\t\t\t\t<label>Category</label>\n\t\t\t\t\t\t<select class=\"custom-select\" id=\"category\">\n\t\t\t\t\t\t\t<option selected>Open this select menu</option>\n\t\t\t\t\t\t\t<option value=\"1\">Informational</option>\n\t\t\t\t\t\t\t<option value=\"2\">Entertainment</option>\n\t\t\t\t\t\t\t<option value=\"3\">News</option>\n\t\t\t\t\t\t</select>\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class=\"card-footer text-center\">\n\t\t\t\t\t\t<button class=\"btn btn-success\" type=\"submit\">Submit</button>\n\t\t\t\t\t</div>\n\t\t\t\t</form>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div>"

/***/ }),

/***/ "./src/app/blog-post-form/blog-post-form.component.ts":
/*!************************************************************!*\
  !*** ./src/app/blog-post-form/blog-post-form.component.ts ***!
  \************************************************************/
/*! exports provided: BlogPostFormComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "BlogPostFormComponent", function() { return BlogPostFormComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var src_app_shared_models_blogpost_model__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/app/shared/models/blogpost.model */ "./src/app/shared/models/blogpost.model.ts");



var BlogPostFormComponent = /** @class */ (function () {
    // bp:BlogPost;
    function BlogPostFormComponent() {
    }
    BlogPostFormComponent.prototype.ngOnInit = function () {
    };
    BlogPostFormComponent.prototype.SubmitPost = function (event) {
        event.preventDefault();
        var bp = new src_app_shared_models_blogpost_model__WEBPACK_IMPORTED_MODULE_2__["BlogPost"]();
        bp.header = (event.target.querySelector('#header').value);
        bp.subHeader = (event.target.querySelector('#subheader').value);
        bp.author = (event.target.querySelector('#author').value);
        bp.content = (event.target.querySelector('#content').value);
        bp.hashtags = (event.target.querySelector('#hashtags').value);
        bp.category = (event.target.querySelector('#category').value);
        console.log(bp);
    };
    BlogPostFormComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-blog-post-form',
            template: __webpack_require__(/*! ./blog-post-form.component.html */ "./src/app/blog-post-form/blog-post-form.component.html"),
            styles: [__webpack_require__(/*! ./blog-post-form.component.css */ "./src/app/blog-post-form/blog-post-form.component.css")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], BlogPostFormComponent);
    return BlogPostFormComponent;
}());



/***/ }),

/***/ "./src/app/landingpage/landingpage.component.css":
/*!*******************************************************!*\
  !*** ./src/app/landingpage/landingpage.component.css ***!
  \*******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2xhbmRpbmdwYWdlL2xhbmRpbmdwYWdlLmNvbXBvbmVudC5jc3MifQ== */"

/***/ }),

/***/ "./src/app/landingpage/landingpage.component.html":
/*!********************************************************!*\
  !*** ./src/app/landingpage/landingpage.component.html ***!
  \********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"d-flex mx-auto m-2 align-items-center\" style=\"min-width: 300px; max-width: 900px;\">\n\t<h3 class=\"mr-3\">NEWS!</h3>\n\t<div class=\"border p-2 d-flex \" style=\"min-width: 800px;\">\n\t\t<a class=\"border p-1 m-2\">\n\t\t\t<b>Title</b>\n\t\t\t<p>description</p>\n\t\t\t<p>description</p>\n\t\t</a>\n\t</div>\n</div>\n<br>\n<div class=\"jumbotron jumbotron-fluid\">\n\t<div class=\"container\">\n\t\t<h1 class=\"display-4\">Main Story or Big Logo Presentation</h1>\n\t\t<p class=\"lead\">This is a modified jumbotron that occupies the entire horizontal space of its parent.</p>\n\t</div>\n</div>\n\n<button routerLink=\"/blog-post-form\">Post New Article</button>\n<div class=\"track d-flex\">\n\n\t<section class=\"left col-md-4 bg-primary\">\n\t\t<p>Top Stories</p>\n\t\t<article class=\"ts text-center\">\n\t\t\t<div class=\"\">\n\t\t\t\t<img src=\"https://dummyimage.com/600x400/000/fff\" width=\"100%\" height=\"auto\">\n\t\t\t</div>\n\t\t\t<div class=\"headline\">Headline of the Story</div>\n\t\t</article>\n\t</section>\n\t<section class=\"main col-md-5 bg-secondary p-0\">\n\t\t<article class=\"ms text-center\">\n\t\t\t<div class=\"video\">\n\t\t\t\t<iframe width=\"100%\" height=\"240px\" src=\"https://www.youtube.com/embed/_xRoEXcVDow\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>\n\t\t\t\t<!-- <img src=\"https://dummyimage.com/600x400/000/fff\" width=\"100%\" height=\"auto\"> -->\n\t\t\t</div>\n\t\t\t<!-- <div class=\"caption\">My Latest Video upload</div> -->\n\t\t\t<!-- <div class=\"sub text-left\"><small>date, time, topic, hashtag</small> </div> -->\n\t\t</article>\n\t</section>\n\t<section class=\"right col-md-3 bg-info\">\n\t\t<p>Latest Stories</p>\n\t\t<article class=\"ls text-left\">\n\t\t\t<div class=\"border-bottom pb-2\">Headline of the story</div>\n\t\t</article>\n\t</section>\n</div>"

/***/ }),

/***/ "./src/app/landingpage/landingpage.component.ts":
/*!******************************************************!*\
  !*** ./src/app/landingpage/landingpage.component.ts ***!
  \******************************************************/
/*! exports provided: LandingpageComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "LandingpageComponent", function() { return LandingpageComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var LandingpageComponent = /** @class */ (function () {
    function LandingpageComponent() {
    }
    LandingpageComponent.prototype.ngOnInit = function () {
    };
    LandingpageComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-landingpage',
            template: __webpack_require__(/*! ./landingpage.component.html */ "./src/app/landingpage/landingpage.component.html"),
            styles: [__webpack_require__(/*! ./landingpage.component.css */ "./src/app/landingpage/landingpage.component.css")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], LandingpageComponent);
    return LandingpageComponent;
}());



/***/ }),

/***/ "./src/app/page-not-found/page-not-found.component.css":
/*!*************************************************************!*\
  !*** ./src/app/page-not-found/page-not-found.component.css ***!
  \*************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL3BhZ2Utbm90LWZvdW5kL3BhZ2Utbm90LWZvdW5kLmNvbXBvbmVudC5jc3MifQ== */"

/***/ }),

/***/ "./src/app/page-not-found/page-not-found.component.html":
/*!**************************************************************!*\
  !*** ./src/app/page-not-found/page-not-found.component.html ***!
  \**************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<p>\n  page-not-found works!\n</p>\n"

/***/ }),

/***/ "./src/app/page-not-found/page-not-found.component.ts":
/*!************************************************************!*\
  !*** ./src/app/page-not-found/page-not-found.component.ts ***!
  \************************************************************/
/*! exports provided: PageNotFoundComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "PageNotFoundComponent", function() { return PageNotFoundComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var PageNotFoundComponent = /** @class */ (function () {
    function PageNotFoundComponent() {
    }
    PageNotFoundComponent.prototype.ngOnInit = function () {
    };
    PageNotFoundComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-page-not-found',
            template: __webpack_require__(/*! ./page-not-found.component.html */ "./src/app/page-not-found/page-not-found.component.html"),
            styles: [__webpack_require__(/*! ./page-not-found.component.css */ "./src/app/page-not-found/page-not-found.component.css")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], PageNotFoundComponent);
    return PageNotFoundComponent;
}());



/***/ }),

/***/ "./src/app/shared/models/blogpost.model.ts":
/*!*************************************************!*\
  !*** ./src/app/shared/models/blogpost.model.ts ***!
  \*************************************************/
/*! exports provided: BlogPost, Comment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "BlogPost", function() { return BlogPost; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "Comment", function() { return Comment; });
var BlogPost = /** @class */ (function () {
    function BlogPost(header, subHeader, author, image, content, comments, publishDate, views, hashtags, category) {
        this.header = header;
        this.subHeader = subHeader;
        this.author = author;
        this.image = image;
        this.content = content;
        this.comments = comments;
        this.publishDate = publishDate;
        this.views = views;
        this.hashtags = hashtags;
        this.category = category;
    }
    return BlogPost;
}());

var Comment = /** @class */ (function () {
    function Comment(author, content, publishDate) {
        this.author = author;
        this.content = content;
        this.publishDate = publishDate;
    }
    return Comment;
}());



/***/ }),

/***/ "./src/app/ui/footer/footer.component.css":
/*!************************************************!*\
  !*** ./src/app/ui/footer/footer.component.css ***!
  \************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL3VpL2Zvb3Rlci9mb290ZXIuY29tcG9uZW50LmNzcyJ9 */"

/***/ }),

/***/ "./src/app/ui/footer/footer.component.html":
/*!*************************************************!*\
  !*** ./src/app/ui/footer/footer.component.html ***!
  \*************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<footer>\n\t<nav class=\"navbar bg-dark\">\n\t\t<div class=\"navbar-expand m-auto navbar-text\">\n\t\t\t<div class=\"row\">\n\t\t\t\t<div class=\"col-lg-6 text-center \">\n\t\t\t\t\t<p class=\"text-white small mb-0\">© AirBnB Automated 2019. All Rights Reserved.</p>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"col-lg-6 h-100 text-center text-lg-right my-auto\">\n\t\t\t\t\t<ul class=\"list-inline mb-0\" style=\"color: white;\">\n\t\t\t\t\t\tContact us by <a href=\"mailto:contact@airbnb-auto.com?subject=Give your feedback\">Email AirBnB-Auto</a>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</nav>\n</footer>\n"

/***/ }),

/***/ "./src/app/ui/footer/footer.component.ts":
/*!***********************************************!*\
  !*** ./src/app/ui/footer/footer.component.ts ***!
  \***********************************************/
/*! exports provided: FooterComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "FooterComponent", function() { return FooterComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var FooterComponent = /** @class */ (function () {
    function FooterComponent() {
    }
    FooterComponent.prototype.ngOnInit = function () {
    };
    FooterComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-footer',
            template: __webpack_require__(/*! ./footer.component.html */ "./src/app/ui/footer/footer.component.html"),
            styles: [__webpack_require__(/*! ./footer.component.css */ "./src/app/ui/footer/footer.component.css")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], FooterComponent);
    return FooterComponent;
}());



/***/ }),

/***/ "./src/app/ui/header/header.component.css":
/*!************************************************!*\
  !*** ./src/app/ui/header/header.component.css ***!
  \************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".navbar{\r\n\tbackground-color: #EEEEEf;\r\n\tbox-shadow: 0px -5px 25px black;\r\n}\r\n\r\n\r\n@media screen and (max-width: 768px){\r\n\t.navbar-brand{\r\n\t\tmargin-right: auto;\r\n\t\tmargin-left: auto;\r\n\t}\t\r\n}\r\n\r\n\r\n@media screen and (max-width: 615px){\r\n\tul li{\r\n\t\tmargin-bottom: 10px;\r\n\t}\r\n\t.zebuttons{display: block;\r\n    text-align: center;\r\n\t}\r\n}\r\n\r\n\r\n@media screen and (max-width:705px){\r\n\tul{width: 100%}\r\n}\r\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvdWkvaGVhZGVyL2hlYWRlci5jb21wb25lbnQuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBO0NBQ0MsMEJBQTBCO0NBQzFCLGdDQUFnQztDQUNoQzs7O0FBR0Q7Q0FDQztFQUNDLG1CQUFtQjtFQUNuQixrQkFBa0I7RUFDbEI7Q0FDRDs7O0FBRUQ7Q0FDQztFQUNDLG9CQUFvQjtFQUNwQjtDQUNELFdBQVcsZUFBZTtJQUN2QixtQkFBbUI7RUFDckI7Q0FDRDs7O0FBRUQ7Q0FDQyxHQUFHLFdBQVcsQ0FBQztDQUNmIiwiZmlsZSI6InNyYy9hcHAvdWkvaGVhZGVyL2hlYWRlci5jb21wb25lbnQuY3NzIiwic291cmNlc0NvbnRlbnQiOlsiLm5hdmJhcntcclxuXHRiYWNrZ3JvdW5kLWNvbG9yOiAjRUVFRUVmO1xyXG5cdGJveC1zaGFkb3c6IDBweCAtNXB4IDI1cHggYmxhY2s7XHJcbn1cclxuXHJcblxyXG5AbWVkaWEgc2NyZWVuIGFuZCAobWF4LXdpZHRoOiA3NjhweCl7XHJcblx0Lm5hdmJhci1icmFuZHtcclxuXHRcdG1hcmdpbi1yaWdodDogYXV0bztcclxuXHRcdG1hcmdpbi1sZWZ0OiBhdXRvO1xyXG5cdH1cdFxyXG59XHJcblxyXG5AbWVkaWEgc2NyZWVuIGFuZCAobWF4LXdpZHRoOiA2MTVweCl7XHJcblx0dWwgbGl7XHJcblx0XHRtYXJnaW4tYm90dG9tOiAxMHB4O1xyXG5cdH1cclxuXHQuemVidXR0b25ze2Rpc3BsYXk6IGJsb2NrO1xyXG4gICAgdGV4dC1hbGlnbjogY2VudGVyO1xyXG5cdH1cclxufVxyXG5cclxuQG1lZGlhIHNjcmVlbiBhbmQgKG1heC13aWR0aDo3MDVweCl7XHJcblx0dWx7d2lkdGg6IDEwMCV9XHJcbn0iXX0= */"

/***/ }),

/***/ "./src/app/ui/header/header.component.html":
/*!*************************************************!*\
  !*** ./src/app/ui/header/header.component.html ***!
  \*************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<header>\n\t<nav class=\"navbar navbar-light bg-dark static-top p-0 \">\n\t\t<div class=\"container-fluid justify-content-center\">\n\t\t\t<a class=\"navbar-brand\" routerLink=\"/home\">\n\t\t\t\t<img src=\"assets/images/logo.png\" width=\"230\" height=\"90\" alt=\"AirBnB Automated Logo\">\n\t\t\t</a>\n\t\t\t<ul class=\"list-inline mb-2 d-flex\" style=\"color: black\">\n\t\t\t\t<div class=\"litty mr-2 align-items-center d-flex flex-wrap\">\n\t\t\t\t</div>\n\t\t\t</ul>\n\t\t</div>\n\t</nav>\n</header>\n"

/***/ }),

/***/ "./src/app/ui/header/header.component.ts":
/*!***********************************************!*\
  !*** ./src/app/ui/header/header.component.ts ***!
  \***********************************************/
/*! exports provided: HeaderComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HeaderComponent", function() { return HeaderComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var HeaderComponent = /** @class */ (function () {
    function HeaderComponent() {
    }
    HeaderComponent.prototype.ngOnInit = function () {
    };
    HeaderComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-header',
            template: __webpack_require__(/*! ./header.component.html */ "./src/app/ui/header/header.component.html"),
            styles: [__webpack_require__(/*! ./header.component.css */ "./src/app/ui/header/header.component.css")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], HeaderComponent);
    return HeaderComponent;
}());



/***/ }),

/***/ "./src/app/ui/layout/layout.component.css":
/*!************************************************!*\
  !*** ./src/app/ui/layout/layout.component.css ***!
  \************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL3VpL2xheW91dC9sYXlvdXQuY29tcG9uZW50LmNzcyJ9 */"

/***/ }),

/***/ "./src/app/ui/layout/layout.component.html":
/*!*************************************************!*\
  !*** ./src/app/ui/layout/layout.component.html ***!
  \*************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<app-header></app-header>\n<div>\n  <ng-content></ng-content>\n</div>\n<app-footer></app-footer>\n"

/***/ }),

/***/ "./src/app/ui/layout/layout.component.ts":
/*!***********************************************!*\
  !*** ./src/app/ui/layout/layout.component.ts ***!
  \***********************************************/
/*! exports provided: LayoutComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "LayoutComponent", function() { return LayoutComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var LayoutComponent = /** @class */ (function () {
    function LayoutComponent() {
    }
    LayoutComponent.prototype.ngOnInit = function () {
    };
    LayoutComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-layout',
            template: __webpack_require__(/*! ./layout.component.html */ "./src/app/ui/layout/layout.component.html"),
            styles: [__webpack_require__(/*! ./layout.component.css */ "./src/app/ui/layout/layout.component.css")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], LayoutComponent);
    return LayoutComponent;
}());



/***/ }),

/***/ "./src/app/ui/ui.module.ts":
/*!*********************************!*\
  !*** ./src/app/ui/ui.module.ts ***!
  \*********************************/
/*! exports provided: UiModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UiModule", function() { return UiModule; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/fesm5/common.js");
/* harmony import */ var _header_header_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./header/header.component */ "./src/app/ui/header/header.component.ts");
/* harmony import */ var _footer_footer_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./footer/footer.component */ "./src/app/ui/footer/footer.component.ts");
/* harmony import */ var _layout_layout_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./layout/layout.component */ "./src/app/ui/layout/layout.component.ts");






var UiModule = /** @class */ (function () {
    function UiModule() {
    }
    UiModule = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"])({
            declarations: [
                _header_header_component__WEBPACK_IMPORTED_MODULE_3__["HeaderComponent"],
                _footer_footer_component__WEBPACK_IMPORTED_MODULE_4__["FooterComponent"],
                _layout_layout_component__WEBPACK_IMPORTED_MODULE_5__["LayoutComponent"],
            ],
            exports: [
                _header_header_component__WEBPACK_IMPORTED_MODULE_3__["HeaderComponent"],
                _footer_footer_component__WEBPACK_IMPORTED_MODULE_4__["FooterComponent"],
                _layout_layout_component__WEBPACK_IMPORTED_MODULE_5__["LayoutComponent"],
            ],
            imports: [
                _angular_common__WEBPACK_IMPORTED_MODULE_2__["CommonModule"]
            ]
        })
    ], UiModule);
    return UiModule;
}());



/***/ }),

/***/ "./src/environments/environment.ts":
/*!*****************************************!*\
  !*** ./src/environments/environment.ts ***!
  \*****************************************/
/*! exports provided: environment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "environment", function() { return environment; });
// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
var environment = {
    production: false
};
/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.


/***/ }),

/***/ "./src/main.ts":
/*!*********************!*\
  !*** ./src/main.ts ***!
  \*********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/platform-browser-dynamic */ "./node_modules/@angular/platform-browser-dynamic/fesm5/platform-browser-dynamic.js");
/* harmony import */ var _app_app_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app/app.module */ "./src/app/app.module.ts");
/* harmony import */ var _environments_environment__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./environments/environment */ "./src/environments/environment.ts");




if (_environments_environment__WEBPACK_IMPORTED_MODULE_3__["environment"].production) {
    Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["enableProdMode"])();
}
Object(_angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__["platformBrowserDynamic"])().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_2__["AppModule"])
    .catch(function (err) { return console.error(err); });


/***/ }),

/***/ 0:
/*!***************************!*\
  !*** multi ./src/main.ts ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! C:\Users\JT-PC\Desktop\Push-Drive\DayWon\S.Rakidzich\AirBNB-blog\src\main.ts */"./src/main.ts");


/***/ })

},[[0,"runtime","vendor"]]]);
//# sourceMappingURL=main.js.map