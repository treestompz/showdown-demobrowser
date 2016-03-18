var db = angular.module('demoBrowser', [])

db.controller('DemoCtrl', function($scope, $http, $interval) {

    $http.get("/api/get_demos")
        .success(function(data) {
            $scope.servers = [];
            angular.forEach(data.demos, function(v, k) {
                var servObj = {};
                servObj.name = v.server_name;
                servObj.demos = v.server_demos;
                $scope.servers.push(servObj);
            });
            console.log($scope.servers);
        })
        .error(function(data) {
            console.log(data);
        })

    $interval(function() {
        $http.get("/api/get_demos")
            .success(function(data) {
                $scope.servers = [];
                angular.forEach(data.demos, function(v, k) {
                    var servObj = {};
                    servObj.name = v.server_name;
                    servObj.demos = v.server_demos;
                    $scope.servers.push(servObj);
                });
                console.log($scope.servers);
            })
            .error(function(data) {
                console.log(data);
            })
    }, 5000);

});



db.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});
