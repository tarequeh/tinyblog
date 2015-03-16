'use strict';

angular.module('TinyBlogApp', [
    'TinyBlogApp.services',
    'TinyBlogApp.controllers',
    'ngRoute'
]).
config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when("/articles/:page?", {
            templateUrl: "static/partials/articles.html",
            controller: "articlesController"
        }).
        when("/article/:id", {
            templateUrl: "static/partials/article.html",
            controller: "articleController"
        }).
        otherwise({redirectTo: '/articles'});
}]);
