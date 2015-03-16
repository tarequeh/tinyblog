'use strict';

angular.module('TinyBlogApp.services', []).
    factory('tinyBlogAPIservice', function($http) {
        var tinyBlogAPI = {};

        tinyBlogAPI.getArticles = function (page) {
            return $http({
                method: 'GET',
                url: '/api/article/?page=' + page
            });
        };

        tinyBlogAPI.getArticle = function (id) {
            return $http({
                method: 'GET',
                url: '/api/article/' + id + '/'
            });
        };

        return tinyBlogAPI;
    });
