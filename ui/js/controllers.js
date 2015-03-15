'use strict';

angular.module('TinyBlogApp.controllers', []).
    /* Articles controller */
    controller('articlesController', function($scope, tinyBlogAPIservice) {
        $scope.count = null;
        $scope.next = null;
        $scope.previous = null;
        $scope.articles = [];

        tinyBlogAPIservice.getArticles().success(function (response) {
            $scope.count = response.count;
            $scope.next = response.next;
            $scope.previous = response.previous;
            $scope.articles = response.results;
        });
    }).

    /* Article controller */
    controller('articleController', function($scope, $routeParams, tinyBlogAPIservice) {
        $scope.id = $routeParams.id;
        $scope.article = null;

        tinyBlogAPIservice.getArticle($scope.id).success(function (response) {
            $scope.article = response;
        });
    });
