/*
 * Copyright (c) 2014 Personal-Health-Monitoring-System
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * 	http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.cse3310.phms.model.utils;

import com.activeandroid.Model;
import com.activeandroid.annotation.Column;
import com.activeandroid.annotation.Table;
import com.cse3310.phms.model.Diet;
import com.cse3310.phms.model.Food;

public class ManyToManyTable {
    private ManyToManyTable() {}

    /**
     * This class is use to create a many-to-many relationship for the database
     * between Diet and Food.
     */
    @Table(name = "DietAndFood")
    public static class DietAndFood extends Model {
        @Column private Diet diet;
        @Column private Food food;

        public DietAndFood() {
            super();
        }

        public DietAndFood(Diet diet, Food food) {
            this.diet = diet;
            this.food = food;
        }

        public long getDietId() {
            return diet.getId();
        }

        public long getFoodId() {
            return food.getId();
        }
    }
}
