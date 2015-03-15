angular.module('TinyBlogApp', [
    'TinyBlogApp.services',
    'TInyBlogApp.controllers',
    'ngRoute'
]).
config(['$routeProvider', function($routeProvider) {
    'use strict';

    $routeProvider.
        when("/articles", {
            templateUrl: "partials/articles.html",
            controller: "tinyBlogController"
        }).
        when("/article/:id", {
            templateUrl: "partials/article.html",
            controller: "tinyBlogController"
        }).
        otherwise({redirectTo: '/articles'});
}]);
