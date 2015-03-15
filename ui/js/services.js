'use strict';

angular.module('TinyBlogApp.services', []).
    factory('tinyBlogAPIservice', function($http) {
        var tinyBlogAPI = {};

        tinyBlogAPI.getArticles = function() {
            return $http({
                method: 'GET',
                url: '/api/article/'
            });
        };

        tinyBlogAPI.getArticle = function(id) {
            return $http({
                method: 'GET',
                url: '/api/article/'+ id +'/'
            });
        };

        return tinyBlogAPI;
    });
