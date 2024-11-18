//
//  bubble_sort.cpp
//  bubble_sort
//
//  Created by Mateus Felipe da Silveira Vieira on 29/10/24.
//

// Compilado com: clang++ -shared -Wl,-install_name,testlib.so -o bubble_sort.so -fPIC bubble_sort.cpp


/*
 Copyright ©️ 2024 Mateus Felipe da Silveira Vieira
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>5.
 
 */


#include "bubble_sort.hpp"
#include <iostream>
#include <vector>

using namespace std;
extern "C" {
    float * bubble_sort(float vec[], float len){
        //cout << len << endl;
        for(int i = 0; i < len - 1; i++){
            for(int j = 0; j < len - 1; j++){
                float tmp;
                if(vec[j] > vec[j + 1]){
                    tmp = vec[j];
                    vec[j] = vec[j + 1];
                    vec[j + 1] = tmp;
                }
                //cout << "i: " << i << " j: " << j << endl;
            
            }
        }
        return vec;
    }
}
